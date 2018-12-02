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




turtle.hideturtle()
turtle.penup()



turtle.begin_poly()
for i in range(6):
	turtle.forward(50)
	turtle.right(60)
turtle.end_poly()
hexagon = turtle.get_poly()
register_shape("Hexagon", hexagon)




judeh = turtle.Turtle()
judeh.shape("Hexagon")
judeh.penup()
judeh.goto(100,100)









class Hexagon(Turtle):	
	def __init__(self, size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("Hexagon")

hexa = Hexagon(5)


turtle.mainloop()