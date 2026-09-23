"""Minimal Ollama HTTP client (stdlib-friendly via requests)."""
from __future__ import print_function

import os

try:
    import requests
except ImportError:
    raise SystemExit("Please install requests: pip install -r requirements.txt")

DEFAULT_BASE = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
DEFAULT_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")


def list_models(base_url=DEFAULT_BASE, timeout=30):
    r = requests.get(base_url.rstrip("/") + "/api/tags", timeout=timeout)
    r.raise_for_status()
    return r.json()


def chat(messages, model=DEFAULT_MODEL, base_url=DEFAULT_BASE, timeout=120):
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
    }
    r = requests.post(
        base_url.rstrip("/") + "/api/chat",
        json=payload,
        timeout=timeout,
    )
    r.raise_for_status()
    data = r.json()
    return data.get("message", {}).get("content", "")


def ping(base_url=DEFAULT_BASE, timeout=5):
    try:
        list_models(base_url=base_url, timeout=timeout)
        return True
    except Exception:
        return False
