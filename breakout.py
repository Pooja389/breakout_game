from turtle import *
import time
screen = Screen()

screen.setup(width = 600,height = 400)
screen.bgcolor("black")
screen.title("breakout")
screen.tracer(0)

paddle = Turtle()
paddle.shapesize(1,7)
paddle.penup()
paddle.color("white")
paddle.shape("square")
paddle.goto(-240,-180)

ball = Turtle()
ball.shape("circle")
ball.color("blue")
ball.goto(0,0)
ball.shapesize(1.5)
ball.dx = 3
ball.dy = 3

game_over_text = Turtle()
game_over_text.hideturtle()
game_over_text.penup()
game_over_text.pencolor("red")
game_over_text.goto(0,0)


blocks = []
for i in range(16):
    block = Turtle()
    block.shape("square")
    block.penup()
    block.shapesize(2,4)
    block.color("red")
    
    if i < 8:
        block.speed(0)
        block.goto(-280 + 80*i,180)
        block.showturtle()
        blocks.append(block)
    if i >= 8:
        i = i - 8
        block.speed(0)
        block.goto(-280 + 80*i,140)    
        block.showturtle()
        blocks.append(block)
    
def move_left():
    x = paddle.xcor()
    x -=50
    paddle.setx(x)

def move_right():
    x = paddle.xcor()
    x +=50
    paddle.setx(x)

screen.listen()
screen.onkey(move_left,"b")
screen.onkey(move_right,"n")

ball.penup()

while True:
    screen.update()
    time.sleep(0.01)
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1
    
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1


    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
    
    if ball.ycor() < -190:
        game_over_text.write("GAME OVER !!",font = ("Helvetica",14,"normal"))
        break

    if (ball.dy < 0) and (paddle.ycor() + 10 > ball.ycor() > paddle.ycor() - 10) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    for block in blocks:
        if block.isvisible() and block.distance(ball)<25:
            block.hideturtle()
            ball.dy *= -1
            blocks.remove(block)
            
            
    if len(blocks) <= 0:
        game_over_text.write("you win!!",font = ("Helvetica",14,"normal"))
        break

    

screen.exitonclick()