from turtle import*
import turtle 
import time

points = 0

timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(0,300)

while True:
    timer.write(str(points), move = True, align = "center", font = ("Arial", 20, "normal"))
    
    time.sleep(1)
    points += 1
    timer.clear()
    timer.goto(0, 300)



def clicked(x,y):
	print("you clicked " + str(x) + "," + str(y))

turtle.onscreenclick(clicked)

turtle.mainloop()
