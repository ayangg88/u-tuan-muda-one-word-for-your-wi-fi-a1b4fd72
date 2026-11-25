#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Writes a single word describing home Wi-Fi as it is actually lived:
there one moment, gone the next, mid-call, mid-game, mid-sentence —
no explanation, no goodbye. The word is the network name.
"""
import os

WORD = "Ghosting"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
