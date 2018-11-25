from turtle import *
import random
import turtle
import math


class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
	

ball1 = Ball(80,"blue", 5)
ball1.penup()
ball1.goto(100,0)
ball1.pendown()
ball2 = Ball(50,"green", 5)




def check_collision(ball1,ball2):
	D = math.sqrt(math.pow((ball2.xcor()-ball1.xcor()),2) + math.pow((ball2.ycor() - ball1.ycor()),2))
	if D >= ball1.radius + ball2.radius:
		print("The balls didn't collide!")
	if D < ball1.radius + ball2.radius:
		print("The balls collided")
check_collision(ball1,ball2)

turtle.mainloop()












