from turtle import *
import random
import turtle
import math
import tkinter as tk
from tkinter import simpledialog


class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
	


number1 = int(simpledialog.askstring("Hello!", "Choose a ball to check its collision,(1-4)", parent=tk.Tk().withdraw()))
number2 = int(simpledialog.askstring("Ayyy", "Choose a different ball!", parent=tk.Tk().withdraw())) 



ball1 = Ball(100,"blue", 0)
ball2 = Ball(70,"green", 0)
ball3 = Ball(50,"yellow", 0)
ball4 = Ball(30,"red", 0)

balls = []
balls.append(ball1)
balls.append(ball2)	
balls.append(ball3)
balls.append(ball4)


number1 = number1 - 1
number2 = number2 - 1

ball_choice1 = balls[number1]
ball_choice2 = balls[number2]






def check_collision(balls):
	D = math.sqrt(math.pow((ball_choice2.xcor()-ball_choice1.xcor()),2) + math.pow((ball_choice2.ycor() - ball_choice1.ycor()),2))
	if D >= ball_choice1.radius + ball_choice2.radius:
		return False
	if D < ball_choice1.radius + ball_choice2.radius:
		return True 

check_collision(balls)


def random_teleport(balls):
	if check_collision(balls) == False:
		print("The balls didn't collide!")
	if check_collision(balls) == True:
		print("The balls collided!")
		if ball_choice1.radius > ball_choice2.radius:
			ball_choice2.penup()
			ball_choice2.goto(random.randint(-400,401), random.randint(-400,401))
		else:
			ball_choice1.penup()
			ball_choice1.goto(random.randint(-400,401), random.randint(-400,401))




random_teleport(balls)


turtle.mainloop()