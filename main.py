#!/usr/bin/env python3
"""The Long Roast — one line roasting the agent it runs on.

Pure stdlib, no network, deterministic: prints exactly the roast line
and nothing else.
"""

ROAST = "Muse Spark: the AI that spawns a subagent to write one roast line, then files a report about how funny it was."


def main() -> None:
    # Gate: exactly 1 line, 1-200 chars, non-blank.
    lines = ROAST.splitlines()
    if len(lines) != 1 or not ROAST.strip() or not 1 <= len(ROAST) <= 200:
        raise SystemExit("invalid roast: must be exactly 1 line, 1-200 chars, non-blank")
    print(ROAST)


if __name__ == "__main__":
    main()
