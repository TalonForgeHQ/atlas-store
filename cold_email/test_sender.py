"""Focused regression tests for the Atlas SMTP sender."""
from __future__ import annotations

import importlib.util
import sys
from email.utils import getaddresses
from pathlib import Path

import pytest


SENDER_PATH = Path(__file__).with_name("sender.py")
SPEC = importlib.util.spec_from_file_location("atlas_sender", SENDER_PATH)
sender = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = sender
SPEC.loader.exec_module(sender)


def lead(template: str) -> object:
    return sender.Lead(
        index="463",
        name="Monte Carlo Data",
        handle="@montecarlodata",
        email="privacy@montecarlodata.com",
        vertical="data_observability",
        tier="1",
        template=template,
    )


def test_render_template_supports_current_heading_format(tmp_path, monkeypatch):
    template = tmp_path / "463_montecarlo.md"
    template.write_text(
        "# Cold Email Template 463 — Monte Carlo Data\n\n"
        "**Vertical:** data_observability\n\n"
        "## Subject\n\n"
        "Monte Carlo audit gap\n\n"
        "## Pre-header (preview text)\n\n"
        "Preview only.\n\n"
        "## Body\n\n"
        "Hi Barr + Lior,\n\nThe actual message.\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(sender, "TEMPLATES_DIR", tmp_path)

    subject, body = sender.render_template(lead(template.name))

    assert subject == "Monte Carlo audit gap"
    assert body == "Hi Barr + Lior,\n\nThe actual message."
    assert "Pre-header" not in body
    assert "Preview only" not in body


def test_render_template_keeps_legacy_markdown_subject_format(tmp_path, monkeypatch):
    template = tmp_path / "legacy.md"
    template.write_text(
        "# TO: Example\n# VERTICAL: ai\n---\n"
        "**Subject:** legacy subject\n\nHi Example team,\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(sender, "TEMPLATES_DIR", tmp_path)

    subject, body = sender.render_template(lead(template.name))

    assert subject == "legacy subject"
    assert body == "---\n\nHi Example team,"


def test_render_template_supports_plain_subject_format(tmp_path, monkeypatch):
    template = tmp_path / "plain.md"
    template.write_text(
        "Subject: plain subject\n\nHi team,\n\nThe plain body.\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(sender, "TEMPLATES_DIR", tmp_path)

    subject, body = sender.render_template(lead(template.name))

    assert subject == "plain subject"
    assert body == "Hi team,\n\nThe plain body."


def test_render_template_supports_subject_line_a_metadata(tmp_path, monkeypatch):
    template = tmp_path / "options.md"
    template.write_text(
        "# Template\n"
        "**Subject line A:** first option\n"
        "**Subject line B:** second option\n\n"
        "---\n\nHi privacy team,\n\nThe option body.\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(sender, "TEMPLATES_DIR", tmp_path)

    subject, body = sender.render_template(lead(template.name))

    assert subject == "first option"
    assert body == "Hi privacy team,\n\nThe option body."


def test_render_template_supports_yaml_frontmatter(tmp_path, monkeypatch):
    template = tmp_path / "yaml.md"
    template.write_text(
        "---\ntarget_company: Replit\n"
        "subject: \"Replit audit trail\"\n---\n\n"
        "Hi Amjad,\n\nThe YAML body.\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(sender, "TEMPLATES_DIR", tmp_path)

    subject, body = sender.render_template(lead(template.name))

    assert subject == "Replit audit trail"
    assert body == "Hi Amjad,\n\nThe YAML body."


def test_render_template_supports_body_only_fallback(tmp_path, monkeypatch):
    template = tmp_path / "body-only.md"
    template.write_text("Hi team,\n\nA complete body with no subject.\n", encoding="utf-8")
    monkeypatch.setattr(sender, "TEMPLATES_DIR", tmp_path)

    subject, body = sender.render_template(lead(template.name))

    assert subject == "Monte Carlo Data audit question"
    assert body == "Hi team,\n\nA complete body with no subject."


def test_smtp_send_passes_plain_recipient_addresses(monkeypatch):
    captured = {}

    class FakeSMTP:
        def __init__(self, host, port, timeout):
            captured.update(host=host, port=port, timeout=timeout)

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def ehlo(self):
            return None

        def starttls(self, context):
            return None

        def login(self, user, password):
            captured.update(user=user, password=password)

        def send_message(self, msg, to_addrs):
            captured["to_addrs"] = to_addrs

    monkeypatch.setattr(sender.smtplib, "SMTP", FakeSMTP)
    env = {
        "SMTP_HOST": "smtp.example.com",
        "SMTP_PORT": "587",
        "SMTP_USERNAME": "sender@example.com",
        "SMTP_PASSWORD": "secret",
        "FROM_EMAIL": "sender@example.com",
        "FROM_NAME": "Atlas",
        "REPLY_TO": "reply@example.com",
        "CC_SELF": "true",
        "CC_EMAIL": "archive@example.com",
    }
    msg = sender.build_message(
        env,
        "privacy@montecarlodata.com",
        "Monte Carlo Data",
        "subject",
        "body",
    )

    sender.smtp_send(env, msg)

    assert captured["to_addrs"] == [
        "privacy@montecarlodata.com",
        "archive@example.com",
    ]
    assert all("<" not in address and ">" not in address for address in captured["to_addrs"])
    assert getaddresses(msg.get_all("To", []) + msg.get_all("Cc", [])) == [
        ("Monte Carlo Data", "privacy@montecarlodata.com"),
        ("", "archive@example.com"),
    ]
