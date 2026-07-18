"""Notifier adapters.

Built-in:
- `LocalLogNotifier`: writes alerts to a JSONL file. Always available.
- `TelegramNotifier`: posts to Telegram via the existing Hermes gateway if a
  bot token is configured. Disabled by default.
"""

from __future__ import annotations

import abc
import json
import os
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

USER_AGENT = "used-car-deal-monitor/1.0"


@dataclass
class Adapter(abc.ABC):
    name: str = ""  # subclasses override
    enabled: bool = True

    @abc.abstractmethod
    def send(self, payload: dict[str, Any]) -> bool:
        ...


class LocalLogNotifier(Adapter):
    """Append every alert to a JSONL file. Returns True once persisted."""
    name = "local"

    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def send(self, payload: dict[str, Any]) -> bool:
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload, default=str) + "\n")
        return True


class TelegramNotifier(Adapter):
    """Send alerts via Telegram Bot API. Token + chat_id come from env or config."""
    name = "telegram"

    def __init__(self, bot_token: Optional[str] = None,
                 chat_id: Optional[str] = None):
        self.bot_token = bot_token or os.environ.get("MONITOR_TG_BOT_TOKEN")
        self.chat_id = chat_id or os.environ.get("MONITOR_TG_CHAT_ID")
        self.enabled = bool(self.bot_token and self.chat_id)

    def send(self, payload: dict[str, Any]) -> bool:
        if not self.enabled:
            return False
        text = self._render(payload)
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = urllib.parse.urlencode({
            "chat_id": self.chat_id,
            "text": text,
            "parse_mode": "MarkdownV2",
            "disable_web_page_preview": "true",
        }).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={
            "User-Agent": USER_AGENT,
            "Content-Type": "application/x-www-form-urlencoded",
        })
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                body = json.loads(r.read().decode("utf-8"))
                return bool(body.get("ok"))
        except Exception:
            return False

    @staticmethod
    def _escape_md(text: str) -> str:
        # Conservative escape for Telegram MarkdownV2
        for ch in r"_*[]()~`>#+-=|{}.!":
            text = text.replace(ch, f"\\{ch}")
        return text

    @classmethod
    def _render(cls, p: dict[str, Any]) -> str:
        v = p.get("vehicle", {})
        flags = p.get("risk_flags", [])
        lines = [
            f"*New flagged listing:* {cls._escape_md(v.get('title', '?'))}",
            f"*Ask:* ${p.get('ask_price', 0):,.0f}",
            f"*Valuation:* ${p.get('valuation_low', 0):,.0f} \\- "
            f"${p.get('valuation_high', 0):,.0f} "
            f"(mid ${p.get('valuation_mid', 0):,.0f}, "
            f"{p.get('valuation_confidence', '?')})",
            f"*Discount to mid:* {p.get('discount_pct', 0):.1f}%",
            f"*Risk score:* {p.get('risk_score', 0)}/100",
        ]
        if flags:
            lines.append("*Flags:*")
            for f in flags[:5]:
                lines.append(f"  \\- {cls._escape_md(f.get('message', ''))}")
        if p.get("url"):
            lines.append(f"[link]({p['url']})")
        lines.append(cls._escape_md(p.get("recommendation", "")))
        return "\n".join(lines)