# Pong Game

A two-player Pong game written in Python with the built-in Turtle graphics module. Play locally in one window, score points by getting the ball past the other paddle, and restart without closing the program.

## Features

- Two-player local gameplay
- W/S controls for Player 1
- Up/Down controls for Player 2
- Ball and paddle collision
- Score tracking
- First-to-5 win condition
- Space-to-restart after a match
- Background color cycles when the ball hits the top or bottom boundary
- Red background when a player misses the ball

## Technologies

- Python 3
- Turtle (standard library)

## How to run

1. Install [Python 3](https://www.python.org/downloads/) if it is not already installed. On Windows, enable **Add python.exe to PATH** during setup.
2. Open a terminal in this project folder.
3. Run:

```bash
python pong.py
```

If `python` is not recognized, try `python3 pong.py`.

No extra packages are required.

## Controls

| Action | Player 1 (left) | Player 2 (right) |
| --- | --- | --- |
| Move paddle up | `W` | `Up` arrow |
| Move paddle down | `S` | `Down` arrow |
| Restart after a win | `Space` | `Space` |

Close the window to quit.

## What I Learned

- **Python classes** — paddles, the ball, and the scoreboard are separate objects with their own behavior.
- **Game loops** — a timed loop updates movement, collisions, and drawing each frame instead of running as fast as the CPU allows.
- **Keyboard events** — Turtle `onkeypress` maps keys to paddle movement and restart.
- **Collision detection** — the ball bounces on paddles and walls using position checks.
- **Game state management** — scores, a game-over flag, restart, and background-color state are tracked while the match is running.
