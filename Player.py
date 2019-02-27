from turtle import *
import turtle
import time 
import random
import math
from functions import *
from tkinter import *


abed = Player (30,30,20)
abed.shape("circle")
abed.shapesize(1)
abed.penup()
turtle.bgpic("tapperbg.gif")

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP
foods=[burger,pizza,sushi]
FOODCOLLISION= False


def up():
	global direction
	direction=UP 
	abed.goto(abed.xcor(), abed.ycor() + 10)

def down():
    global direction
    direction = DOWN
    abed.goto(abed.xcor(), abed.ycor() - 10)

def left():
    global direction
    direction = LEFT
    abed.goto(abed.xcor() - 10, abed.ycor())

def right():
    global direction
    direction = RIGHT
    abed.goto(abed.xcor() + 10, abed.ycor())

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

def collide(ball_a,ball_b):
	x1=ball_a.xcor()
	x2=ball_b.xcor()
	y1=ball_a.ycor()
	y2=ball_b.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if D >= ball_a.r + ball_b.r:
		return False
	if D < ball_a.r + ball_b.r:
		return True

def check_food_collision():
	for f in foods:
		if collide(abed,f) == True:
			while FOODCOLLISION == False and collide(f,table)==False:
				f.goto(abed.xcor()+5,abed.ycor())
				f.showturtle()
	return True

def slide_food():
	for f in foods:
		if collide(f,table) == True:
			FOODCOLLISION = True
			f.goto(table.xcor(),table.ycor())
			f.bk(200)
