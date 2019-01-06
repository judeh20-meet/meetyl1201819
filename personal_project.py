from turtle import *


class Ball(Turtle):
	def __init__(self, x, y, dx ,dy, r, color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.r = r
		self.shapesize(r/10)
		self.color(color)
	def move(self, screen_width, screen_height):
		current_x = self.xcor()
		new_x = current_x + self.dx 
		
		current_y = self.ycor()
		new_y = current_y + self.dy

		right_side = new_x + self.r
		left_side = new_x - self.r
		top_side = new_y + self.r
		bottom_side = new_y - self.r

		self.goto(new_x, new_y)

		if top_side > screen_height or bottom_side < -screen_height:
			self.dx *= -1
		if left_side < -screen_height or right_side > screen_height:
			self.dy *= -1







