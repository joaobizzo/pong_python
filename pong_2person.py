import turtle
# Module for windows users:
import winsound as ws

# Style:

# Setting up:

wn = turtle.Screen()
wn.title("Pong by Joaobizzo")
wn.bgcolor("#14213d")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score:
score_a = 0
score_b = 0

# Paddle A (left):
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#fca311")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B (right):
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#fca311")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball:
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#ffecd1")
ball.penup()
ball.goto(0, 0)
# This set up the speed:
ball.dx = 0.2
ball.dy = 0.2


# Pen:
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0          Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions:
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding (you can put whatever ypu want):
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop:
while True:
    wn.update()

    # Move the ball:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking:
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        ws.PlaySound("funny_bounce.wav", ws.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        ws.PlaySound("funny_bounce.wav", ws.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}          Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ws.PlaySound("coin_sound.wav", ws.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}          Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ws.PlaySound("coin_sound.wav", ws.SND_ASYNC)

    # Paddle and ball colision:
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        ws.PlaySound("funny_bounce.wav", ws.SND_ASYNC)

    if (ball.xcor() <- 340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        ws.PlaySound("funny_bounce.wav", ws.SND_ASYNC)




