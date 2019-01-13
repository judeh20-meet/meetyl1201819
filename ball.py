
from turtle import *


class Ball(Turtle):
	def __init__(self, x, y, dx ,dy, r, color):
		Turtle.__init__(self)
		self.penup()
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.r = r
		self.shapesize(r/10)
		self.color(color)
		self.goto(x,y)
	def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
		current_x = self.xcor()
		new_x = current_x + self.dx 
		
		current_y = self.ycor()
		new_y = current_y + self.dy

		right_side = new_x + self.r
		left_side = new_x - self.r
		top_side = new_y + self.r
		bottom_side = new_y - self.r

		self.goto(new_x, new_y)

		if top_side > SCREEN_HEIGHT or bottom_side < -SCREEN_HEIGHT:
			self.dy *= -1
		if left_side < -SCREEN_WIDTH or right_side > SCREEN_WIDTH:
			self.dx *= -1







