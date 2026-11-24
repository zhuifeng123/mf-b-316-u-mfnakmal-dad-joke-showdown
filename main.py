#!/usr/bin/env python3
import os

ENTRY = "I used to hate facial hair, but then it grew on me."

assert len(ENTRY) <= 200

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
