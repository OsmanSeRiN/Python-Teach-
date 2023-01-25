import turtle
import random

window = turtle.Screen()
window.screensize(800, 350)
window.title("FastTurtle")
window.bgcolor("black")

player = turtle.Turtle()
player.color("red")
player.shape("turtle")
player.shapesize(2)
player.penup()
speed=1
score=0


coin = turtle.Turtle()
coin.penup()
coin.color("yellow")
coin.shape("circle")
coin.shapesize(1)
coin.setposition(random.randint(-600,600),random.randint(-300,300))

ScoreTable=turtle.Turtle()
ScoreTable.shape("square")
ScoreTable.color("pink")
ScoreTable.penup()
ScoreTable.hideturtle()
ScoreTable.goto(-400,400)
ScoreTable.write("Score {}".format(score),align="center",font=("courier",20,"normal"))

SpeedTable=turtle.Turtle()
SpeedTable.shape("square")
SpeedTable.color("pink")
SpeedTable.penup()
SpeedTable.hideturtle()
SpeedTable.goto(-400,370)
SpeedTable.write("Speed {}".format(score),align="center",font=("courier",20,"normal"))


def sola():
    player.left(25)


def saga():
    player.right(25)



window.listen()
window.onkey(sola, 'd')
window.onkey(saga, "a")

while True:
    player.forward(speed)
    a=False
     #Karakterin belirlenen duvarlara çarpıp dönmesi
    if player.xcor() > 800 or player.xcor() < -800 :
        player.right(180)
        if speed >0:
          speed = speed - 1
        else:
            speed=0

    if player.ycor() > 350 or player.ycor() < -350:
        player.right(180)
        if speed > 0:
            speed = speed - 1
        else:
            speed = 0

    if player.distance(coin) < 20:
        coin.setposition(random.randint(-300,300),random.randint(-300,300))
        score=score+1
        ScoreTable.clear()
        ScoreTable.write("Score {}".format(score), align="center", font=("Courier", 20, "normal"))
        if score % 5 == 0:
            speed=speed+1
            a=True
    if a == True:
        SpeedTable.clear()
        SpeedTable.write("Speed {}".format(speed), align="center", font=("courier", 20, "normal"))
    #Tamamlanmamış