from turtle import *
import random
import turtle
import math
import tkinter as tk
from tkinter import simpledialog





class Ball(Turtle):
	def __init__(self, x, y, radius, dx, dy):
		Turtle.__init__(self)
		
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.dx = dx
		self.dy = dy
	
	def move():

ball1= Ball(200,200,50,4,5)
ball1.move

turtle.mainloop()