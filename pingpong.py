import turtle

wn=turtle.Screen()
wn.title("PING PONG FIRST DRAFT")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

MAX_SCORE = 5 
score_a = 0
score_b = 0

game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("red")
game_over_pen.penup()
game_over_pen.hideturtle()
game_over_pen.goto(0, 0)

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=0.1

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1:0        Player 2:0",align="center",font=("Courier",24,"bold"))

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

gamerun = True 
while gamerun:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1  

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player 1:{}        Player 2:{}".format(score_a,score_b),align="center",font=("Courier",24,"bold"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player 1:{}        Player 2:{}".format(score_a,score_b),align="center",font=("Courier",24,"bold"))

    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor()< paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor()< paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


    if score_a == MAX_SCORE:
        game_over_pen.write("Player 1 WINS!", align="center", font=("Courier", 36, "bold"))
        ball.dx = 0 
        ball.dy = 0
        gamerun = False
        continue 
    elif score_b == MAX_SCORE:
        game_over_pen.write("Player 2 WINS!", align="center", font=("Courier", 36, "bold"))
        ball.dx = 0 
        ball.dy = 0
        gamerun = False
        continue
          
if not gamerun:
    wn.mainloop()