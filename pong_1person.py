import turtle
# Module for windows users
import winsound as ws


# Setting up:

wn = turtle.Screen()
wn.title("Pong by Joaobizzo")
wn.bgcolor("#14213d")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score:
score = 0

# Paddle:
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("#fca311")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -270)


# Ball:
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#ffecd1")
ball.penup()
ball.goto(0, 200)
# Speed:
ball.dx = 0.16
ball.dy = 0.16


# Pen:
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions:
def paddle_a_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)


def paddle_a_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)


# Keyboard binding:
wn.listen()
wn.onkeypress(paddle_a_right, "Right")
wn.onkeypress(paddle_a_left, "Left")


# Main game loop:
while True:
    wn.update()
    # Move the ball:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking:
    if ball.ycor() < -300:
        ball.goto(0, 200)
        ball.dy *= 1
        pen.clear()
        score = 0
        pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        ws.PlaySound("coin_sound.wav", ws.SND_ASYNC)

    if ball.ycor() > 299:
        ball.sety(290)
        ball.dy *= -1
        ws.PlaySound("funny_bounce.wav", ws.SND_ASYNC)
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 399:
        ball.setx(390)
        ball.dx *= -1
        ws.PlaySound("funny_bounce.wav", ws.SND_ASYNC)

    if ball.xcor() < -399:
        ball.setx(-390)
        ball.dx *= -1
        ws.PlaySound("funny_bounce.wav", ws.SND_ASYNC)

    # Paddle and ball colision:
    if(ball.ycor() < -270 and ball.xcor() > -290) and (ball.xcor() < paddle.xcor() + 40 and ball.xcor() > paddle.xcor() - 40):
        ball.sety(-270)
        ball.dy *= -1
        ws.PlaySound("funny_bounce.wav", ws.SND_ASYNC)
