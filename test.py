from turtle import *
import turtle

class Food(Turtle):
	def __init__(self, x, y, w, h, r):
		Turtle.__init__(self)
		self.penup()
		self.w = w
		self.h = h
		self.r = r
		self.hideturtle()
		self.goto(x,y)

	def top(self):
		return self.ycor()+self.h/2
	def bottom(self):
		return self.ycor()-self.h/2
	def left(self):
		return self.xcor()+self.w/2
	def right(self):
		return self.xcor()-self.w/2
	# def move(self,dx):
	# 	self.dx = dx
	# 	current_x=self.xcor()
	# 	new_x=current_x+self.dx
	# 	current_y=self.ycor()
	# 	while True:
	# 		self.goto(new_x,current_y)

turtle.hideturtle()

turtle.tracer(0)
turtle.register_shape("burger1.gif")
turtle.register_shape("pizzaf.gif")
turtle.register_shape("sushi.gif")
burger = Food (450, 290, 50, 44, 10)
burger.shape("circle")
burger.shape("burger1.gif")
turtle.penup()
pizza = Food (570, 130, 50, 44, 3)
pizza.shape("pizzaf.gif")
sushi = Food (650, -50, 50, 44, 30)
sushi.shape("sushi.gif")
turtle.tracer(1)

class Player(Turtle):
	def __init__(self, w, h, r):
		Turtle.__init__(self)
		self.penup()
		self.goto(0,0)
		self.w=w
		self.h=h
		self.r=r

	def top(self):
		return self.ycor()+self.h/2
	def bottom(self):
		return self.ycor()-self.h/2
	def left(self):
		return self.xcor()+self.w/2
	def right(self):
		return self.xcor()-self.w/2

table=Food (200,280,30,20,40)
table2=Food(200,70,30,20,40)
table3=Food(200,-150,30,20,40)
table4=Food(200,-360,30,20,40)