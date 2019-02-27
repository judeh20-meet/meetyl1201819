from turtle import *
import turtle
import time 
import random
import math

# points = 3
# timer = turtle.Turtle()
# timer.hideturtle()
# timer.penup()
# timer.goto(0,300)
# while points >= 0 :
# 	timer.write(str("GAME STARTS IN: " + str(points) + " SECONDS"), move = True, align = "center", font = ("Arial",20,"normal"))
# 	points-= 1
# 	time.sleep(1)
# 	timer.clear()
# 	timer.goto(0,300)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP
def up():
	global direction
	direction=UP 
	snake.goto(snake.xcor(), snake.ycor() + 10)

def down():
    global direction
    direction = DOWN
    snake.goto(snake.xcor(), snake.ycor() - 10)


def left():
    global direction
    direction = LEFT
    snake.goto(snake.xcor() - 10, snake.ycor())


def right():
    global direction
    direction = RIGHT
    snake.goto(snake.xcor() + 10, snake.ycor())

snake = turtle.Turtle()
# snake.speed(1)
snake.shape("square")
snake.hideturtle()
snake.penup()
snake.goto(400,0)
snake.showturtle()
snake.pendown()


turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.listen()



turtle.mainloop()