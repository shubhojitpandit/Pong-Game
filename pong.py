"""Classic two-player Pong using Python's built-in turtle module."""

import time
import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_SPEED = 40
BALL_SPEED = 4
WIN_SCORE = 5
FRAME_DELAY = 0.016  # about 60 frames per second
BACKGROUND_COLORS = ["black", "navy", "darkgreen", "purple", "teal"]
SCORE_COLOR = "red"
SCORE_FLASH_FRAMES = 20  # keep red on screen long enough to notice


class Paddle(turtle.Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, 0)

    def move_up(self):
        new_y = self.ycor() + PADDLE_SPEED
        if new_y < SCREEN_HEIGHT / 2 - 50:
            self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - PADDLE_SPEED
        if new_y > -SCREEN_HEIGHT / 2 + 50:
            self.sety(new_y)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.dx *= -1


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.left_score, align="center", font=("Courier", 36, "bold"))
        self.goto(100, 240)
        self.write(self.right_score, align="center", font=("Courier", 36, "bold"))

    def point_left(self):
        self.left_score += 1
        self.update()

    def point_right(self):
        self.right_score += 1
        self.update()

    def reset_scores(self):
        self.left_score = 0
        self.right_score = 0
        self.update()

    def show_winner(self, winner):
        self.update()
        self.goto(0, 0)
        self.write(
            f"{winner} player wins!",
            align="center",
            font=("Courier", 24, "bold"),
        )
        self.goto(0, -40)
        self.write(
            "Press Space to play again",
            align="center",
            font=("Courier", 16, "normal"),
        )


def paddle_hit(ball, paddle):
    return (
        abs(ball.xcor() - paddle.xcor()) < 20
        and abs(ball.ycor() - paddle.ycor()) < 50
    )


def main():
    screen = turtle.Screen()
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)

    left_paddle = Paddle(-350)
    right_paddle = Paddle(350)
    ball = Ball()
    scoreboard = Scoreboard()

    game_over = False
    bg_index = 0
    score_flash_frames = 0

    def apply_cycle_background():
        screen.bgcolor(BACKGROUND_COLORS[bg_index])

    def cycle_background():
        nonlocal bg_index
        bg_index = (bg_index + 1) % len(BACKGROUND_COLORS)
        if score_flash_frames == 0:
            apply_cycle_background()

    def flash_score_background():
        nonlocal score_flash_frames
        screen.bgcolor(SCORE_COLOR)
        score_flash_frames = SCORE_FLASH_FRAMES

    def restart():
        nonlocal game_over, bg_index, score_flash_frames
        if not game_over:
            return
        left_paddle.goto(-350, 0)
        right_paddle.goto(350, 0)
        ball.goto(0, 0)
        ball.dx = BALL_SPEED
        ball.dy = BALL_SPEED
        scoreboard.reset_scores()
        bg_index = 0
        score_flash_frames = 0
        apply_cycle_background()
        game_over = False

    screen.listen()
    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")
    screen.onkeypress(restart, "space")

    while True:
        if not game_over:
            ball.move()

            if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()
                cycle_background()

            if paddle_hit(ball, right_paddle) and ball.dx > 0:
                ball.bounce_x()
            if paddle_hit(ball, left_paddle) and ball.dx < 0:
                ball.bounce_x()

            if ball.xcor() > 390:
                flash_score_background()
                scoreboard.point_left()
                ball.reset_position()
            elif ball.xcor() < -390:
                flash_score_background()
                scoreboard.point_right()
                ball.reset_position()

            if scoreboard.left_score >= WIN_SCORE or scoreboard.right_score >= WIN_SCORE:
                winner = "Left" if scoreboard.left_score >= WIN_SCORE else "Right"
                scoreboard.show_winner(winner)
                game_over = True

        if score_flash_frames > 0:
            score_flash_frames -= 1
            if score_flash_frames == 0:
                apply_cycle_background()

        screen.update()
        time.sleep(FRAME_DELAY)


if __name__ == "__main__":
    main()
