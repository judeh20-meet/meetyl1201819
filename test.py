from turtle import *
import turtle


turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle4 = turtle.Turtle()
turtle5 = turtle.Turtle()
turtle6 = turtle.Turtle()
turtle7 = turtle.Turtle()
turtle8 = turtle.Turtle()

turtles = [turtle1,turtle2,turtle3,turtle4,turtle5,turtle6,turtle7,turtle8]
number = 0
for i in turtles:
	i.goto(number, 100)
	number+=10

	del turtles[3]



turtle.mainloop()