from turtle import *
import turtle
import time 
import random
import math
from functions import *
from tkinter import *
from characters import *

turtle.tracer(100,1)

abed = Player (20)
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
table=Food(200,280,40)
table2=Food(200,70,40)
table3=Food(200,-150,40)
table4=Food(200,-360,40)
tables = [table,table2,table3,table4]
number = 0

def up():
	global direction
	direction=UP 
	abed.goto(abed.xcor(), abed.ycor() + 25)

def down():
    global direction
    direction = DOWN
    abed.goto(abed.xcor(), abed.ycor() - 25)

def left():
    global direction
    direction = LEFT
    abed.goto(abed.xcor() - 25, abed.ycor())

def right():
    global direction
    direction = RIGHT
    abed.goto(abed.xcor() + 25, abed.ycor())

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
			f.showturtle()
			f.goto(abed.xcor(),abed.ycor())
				
	return True

def slide_food():
	for f in foods:
		for t in tables:
			if collide(f,t) == True:
				f.goto(t.xcor(),t.ycor())
				f.move_food()


def check_player_food_collision():
	players = getplayers()
	for f in foods:
		for p in players:
			if collide(f,p) == True:
				f.hideturtle()
				if f == pizza:
					f.goto(570,130)
				elif f == sushi:
					f.goto(650,-50)
				else:
					f.goto(450,290)
	return True

turtle.listen()
frame = 0

while True:	
	check_food_collision()
	frame+=1
	if frame/1500 == 1:
		frame = 0
		spawn_player()
	move_players()
	check_loss()
	check_player_food_collision()
	slide_food()
	turtle.update()
turtle.mainloop()
