import turtle

turtle.addshape("Emoji.gif")
turtle.shape("Emoji.gif")
angle1 = 1
turtle.speed(0)
turtle.tracer(100)


for i in range(100000):
	turtle.right(angle1)
	turtle.forward(100)
	turtle.right(35)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(40)
	angle1 = angle1 + 1
	turtle.penup()
	turtle.home()
	turtle.pendown()






















turtle.mainloop()