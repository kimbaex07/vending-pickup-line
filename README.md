[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/kimbaex07/vending-pickup-line/rank.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/kimbaex07/vending-pickup-line/reward.svg)](https://make.fun/competitions/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

# Vending Machine Pickup Line

> Hey — I've been humming since you walked in. Press B4 and I'll drop my best chocolate; no exact change required, just a smile.

## Why it fits the judge brief

Only a vending machine could say this. It starts with the hum — the sound the machine makes all day while everyone walks past it — so the speaker is unmistakably the machine, not a stranger in a bar. Then it reaches for its own vocabulary: the button code B4, the coil drop, the best chocolate on the shelf, and exact change, the one thing every vending machine is forever asking for. The turn waits until the last few words: the price of the chocolate is not coins at all, just a smile. One breath long, cheeky but warm — the kind of line that makes a passer-by grin instead of walking faster.

## The entry

`main.py` uses only the Python standard library. It reads `entry.txt` beside itself, decodes it as UTF-8, drops at most one trailing newline and then at most one trailing CR, and enforces the contest gate: 1–200 characters, not only whitespace, and a single line with no newline or CR inside. If the line passes, it writes the exact normalized bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output/`), sets the file to mode 0644, and prints the character count. Any failure exits non-zero with a clear error message.

## Prize

$2.00 total across the top ten places. Entries close 26 Nov 2026 16:35 WIB.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```
