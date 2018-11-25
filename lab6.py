from turtle import Turtle
import random
from turtle import *
import turtle

colormode(255)

class Square(Turtle):	
	def __init__(self, size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)

	def random_color(self):
		rgb = (random.randint(0,256), random.randint(0,256), random.randint(0,256))
		self.fillcolor(rgb)
		self.pencolor(rgb)


Jimmy = Square(10)
Jimmy.random_color()
turtle.mainloop()






class Hexagon(Turtle):	
	def __init__(self, size):
		Turtle.__init__(self)


