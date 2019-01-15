from turtle import *
import turtle
import time
import random
from ball import Ball
import math
import time




#making the barrier
barrier = turtle.Turtle()
barrier.hideturtle()
barrier.speed(0)
barrier.penup()
barrier.pensize(5)
barrier.goto(480,0)
barrier.pendown()
barrier.goto(480,-405)
barrier.goto(-480,-405)
barrier.goto(-480,405)
barrier.goto(480,405)
barrier.goto(480,0)



#variables
turtle.tracer(0,0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077  
SCREEN_WIDTH = turtle.getcanvas() . winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas() . winfo_height()/2
player = Ball(0, 0, 25, 25, 15, "blue")
NUMBER_OF_BALLS = 30
MINIMUM_BALL_RADIUS = 5
MAXIMUM_BALL_RADIUS = 20
MINIMUM_BALL_DX = -3
MAXIMUM_BALL_DX = 3
MINIMUM_BALL_DY = -3
MAXIMUM_BALL_DY = 3
BALLS = []
FOOD = []







#creating the circles
for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	r  = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.random(),random.random(),random.random())
	while dx == 0:
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	while dy == 0:
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	new_ball = Ball(x,y,dx,dy,r,color)
	BALLS.append(new_ball)








#checking collisions between 2 balls
def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	current_x1 = ball_a.xcor()
	current_y1 = ball_a.ycor()

			
	current_x2 = ball_b.xcor()
	current_y2 = ball_b.ycor()

	D = math.sqrt(math.pow((current_x2-current_x1),2) + math.pow((current_y2 - current_y1),2))	
	if D >= ball_a.r + ball_b.r:
		return False
	if D < ball_a.r + ball_b.r:
		return True 

	
def check_all_balls():
		for ball_a in BALLS:			
			for ball_b in BALLS:
				collide(ball_a, ball_b)
				
				if collide(ball_a,ball_b) == True:
					r1 = ball_a.r
					r2 = ball_b.r

					x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
					y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
					dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
					dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
					r  = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
					color = (random.random(),random.random(),random.random())
					while dx == 0:
						dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
					while dy == 0:
						dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
					if r1 > r2:
						if r1 < 200:
							ball_a.r = ball_a.r + 3
							ball_a.shapesize(ball_a.r/10)
							ball_b.shapesize(ball_b.r/10)
							
						
							ball_b.goto(x,y)
							ball_b.color(color)
							


					


def myball_collision():
		
		for ball_a in BALLS:
			collide(ball_a, player)
			if collide(ball_a, player) == True:
				if ball_a.r > player.r:
					quit()
				
				if ball_a.r < player.r:
					if player.r < 200:
						x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
						y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
						dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
						dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
						r  = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
						color = (random.random(),random.random(),random.random())
						while dx == 0:
							dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
						while dy == 0:
							dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
						ball_a.goto(x,y)
						player.r = player.r + 1
						player.shapesize(player.r/10)
						ball_a.shapesize(ball_a.r/10)
						ball_a.color(color)
						return True


#making the game move 
def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)
			
def movearound(event):
	player.goto(event.x - SCREEN_WIDTH, SCREEN_HEIGHT - event.y)

turtle.getcanvas() .bind("<Motion>", movearound)

while RUNNING:
	move_all_balls()
	myball_collision()
	check_all_balls()

	turtle.update()
	time.sleep(SLEEP)