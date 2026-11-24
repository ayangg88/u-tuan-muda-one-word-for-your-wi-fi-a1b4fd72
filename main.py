#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Writes a single word describing home Wi-Fi as it is actually lived:
there one moment, gone the next, mid-call, mid-game, mid-sentence —
no explanation, no goodbye. The word is the network name.
"""
import os

WORD = "Ghosting"


def main():
    word = WORD.strip()
    assert 1 <= len(word.encode("utf-8")) <= 20, "word must be 1-20 UTF-8 chars"
    assert len(word.split()) == 1, "word must be a single word"
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(word)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
