#hello horld this is a simple ping pong game by python | 
# i wish to send my your opinion about this and what should add in this game |


#import place:
import turtle

#game screen
wind = turtle.Screen()
wind.title('PING PONG BADR')
wind.bgcolor('orange')
wind.setup(width=900,height=500)
wind.tracer(0)

#player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape('square')
player1.shapesize(stretch_wid=5,stretch_len=1)
player1.color('blue')
player1.penup()
player1.goto(-400,0)


#player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape('square')
player2.shapesize(stretch_wid=5,stretch_len=1)
player2.color('red')
player2.penup()
player2.goto(400,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('black')
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

#score
score1 = 0
score2 = 0 
score = turtle.Turtle()
score.speed(0)
score.color('green')
score.penup()
score.hideturtle()
score.goto(0,200)
score.write('player 1: 0 | player 2: 0', align='center',font=('courier',24,'normal'))

#functions
        #player1_func
def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def player1_down():
    y = player1.ycor()
    y += -20
    player1.sety(y)
        #player2_func
def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)

def player2_down():
    y = player2.ycor()
    y += -20
    player2.sety(y)


#keyboard_player1
wind.listen()
wind.onkeypress(player1_up,'w')
wind.onkeypress(player1_down,'s')

#keyboard_player2
wind.onkeypress(player2_up,'p')
wind.onkeypress(player2_down,'l')

#main game loop
while True:
    wind.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border_check
    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1

    if ball.ycor() < -240:
        ball.sety(-240)
        ball.dy *= -1

    if ball.xcor() > 450:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.write('player 1: {} | player 2: {}'.format(score1,score2), align='center',font=('courier',24,'normal'))

    if ball.xcor() < -450:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.write('player 1: {} | player 2: {}'.format(score1,score2), align='center',font=('courier',24,'normal'))

    #when the ball touch player 2
    if (ball.xcor() > 380 and ball.xcor() < 390 ) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40 ):
        ball.setx(380)
        ball.dx *= -1

    #when the ball touch player 1
    if (ball.xcor() < -380 and ball.xcor() > -390 ) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40 ):
        ball.setx(-380)
        ball.dx *= -1
