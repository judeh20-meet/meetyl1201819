#main folder, where all the game is
from turtle import *
import turtle
import time 
import random
import math
from functions import *
from tkinter import *
from characters import *


#higher tracer = faster characters spawning from the left
turtle.tracer(125,1)

#main character is Abed
abed = Player (20)
abed.shape("circle")
abed.shapesize(1)
abed.penup()

turtle.bgpic("tapperbg.gif")

#life is how many times 
Life = 3

#controls for the player
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP


#creating the tables to place food on
foods=[burger,pizza,sushi]
FOODCOLLISION= False
table=Food(200,280,40)
table2=Food(200,70,40)
table3=Food(200,-150,40)
table4=Food(200,-360,40)
tables = [table,table2,table3,table4]


#controls
def up():
	global direction
	direction=UP 
	abed.goto(abed.xcor(), abed.ycor() + 55)#change this value to change the speed at Abed moves
def down():
    global direction
    direction = DOWN
    abed.goto(abed.xcor(), abed.ycor() - 55)#change this value to change the speed at Abed moves

def left():
    global direction
    direction = LEFT
    abed.goto(abed.xcor() - 55, abed.ycor())#change this value to change the speed at Abed moves

def right():
    global direction
    direction = RIGHT
    abed.goto(abed.xcor() + 55, abed.ycor())#change this value to change the speed at Abed moves

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")


#making the collide function, essential for the rest of the game
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



#checking if Abed has collided with the food on the right 
def check_food_collision():
	for f in foods:
		if collide(abed,f) == True:
			#showing the food whenever Abed touches it
			f.showturtle()
			#making the food follow abed whenever he picks them up
			f.goto(abed.xcor(),abed.ycor())
			
				
	return True


#checking if the food has collided with the tables and making sure they are alligned for desire_food_player collsion
def slide_food():
	global number
	for f in foods:
		for t in tables:
			if collide(f,t) == True:
				#making the food go to the begining of the table
				f.goto(t.xcor(),t.ycor())
				#making the food move a bit to the left whenever it touches the table
				f.bk(50)

	return True


#biggest function, checking the collision between customer requests, the customers, and the food
def check_food_desire_player_collision():
	global Life
	for a in foods:
		for b in desires:
			for c in players:
				if collide(a,c) == True and collide(a,b):
					#checking if the food given to the customer is the correct one
					if a.shape() == b.shape():
						#hiding the food giving the impression a customer is "satisfied"
						a.hideturtle()
						#random value to decide new picture for customers
						e = random.randint(0,4)
						c.shape(shapes[e])
						#random value to decide the new position the customer will go to
						p = random.randint(0,3)
						c.goto(starting_positions[p])
						#random value to decide new customer request
						g = random.randint(0,2)
						b.shape(food_choices[g])
						#making the request of the customer follow the customer
						b.goto(c.xcor()+90, c.ycor()-50)
						#after the food collides, it goes back to its starting positions on the right
						if a == pizza:
							a.goto(570,130)
						elif a == sushi:
							a.goto(650,-50)
						else:
							a.goto(450,290)


					else:
						#same as top except we subtract a point from life
						Life -= 1
						a.hideturtle()
						e = random.randint(0,4)
						c.shape(shapes[e])
						p = random.randint(0,3)
						c.goto(starting_positions[p])
						g = random.randint(0,2)
						b.shape(food_choices[g])
						b.goto(c.xcor()+90, c.ycor()-50)
						if a == pizza:
							a.goto(570,130)
						elif a == sushi:
							a.goto(650,-50)
						else:
							a.goto(450,290)


#this funcion checks if the customers have reached too far on the table and they sacrifice a Life
def check_if_player_reached_table():
	global Life
	for a in desires:
		for b in players:
			if a.xcor() > 200 and b.xcor() > 150:
				Life -= 1
				e = random.randint(0,4)
				b.shape(shapes[e])
				p = random.randint(0,3)
				b.goto(starting_positions[p])
				g = random.randint(0,2)
				a.shape(food_choices[g])
				a.goto(b.xcor()+90, b.ycor()-50)

#listen so the keys can control Abed		
turtle.listen()

frame = 0


#main loop to make game move
while Life > 0:	
	check_food_collision()
	frame+=1
	#change the value in frame/x to control how often players spawn
	if frame/2000 == 1:
		frame = 0
		spawn_player()
	move_players()
	move_desires()
	check_food_desire_player_collision()
	check_if_player_reached_table()
	slide_food()
	turtle.update()
#this section plays whenever you lose







turtle.mainloop()