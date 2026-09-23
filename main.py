# -*- coding: utf-8 -*-
"""Entry: call local Ollama and print one reply."""
from __future__ import print_function

import sys

from src.ollama_client import DEFAULT_MODEL, chat, ping


def main():
    if not ping():
        print(
            "Ollama unreachable at http://localhost:11434. "
            "Start Ollama, then retry.",
            file=sys.stderr,
        )
        return 1

    prompt = "用一句话介绍你自己"
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])

    reply = chat(
        messages=[{"role": "user", "content": prompt}],
        model=DEFAULT_MODEL,
    )
    print(reply)
    return 0


if __name__ == "__main__":
    sys.exit(main())
