from turtle import *
import turtle
import random
import time


sc = turtle.Screen()
sc.setup(1700,1080)
turtle.bgpic("tapperbg.gif")



turtle.register_shape("joyce.gif")
turtle.register_shape("km.gif")
turtle.register_shape("mahd.gif")
turtle.register_shape("sadeen.gif")
turtle.register_shape("shawerma.gif")
shapes = ["joyce.gif", "km.gif", "mahd.gif", "sadeen.gif", "shawerma.gif"]



starting_positions = []
start_pos1 = (-800,335)
starting_positions.append(start_pos1)
start_pos2 = (-800,135)
starting_positions.append(start_pos2)
start_pos3 = (-800,-75)
starting_positions.append(start_pos3)
start_pos4 = (-800,-285)
starting_positions.append(start_pos4)


class Players(Turtle):
	def __init__(self,dx,dy,r):
		Turtle.__init__(self)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.penup()
		self.shape("circle")
		self.shapesize(1)
		self.speed(0)
	
	def move(self):
		self.forward(.1)
	



players = []

			
p = 0
def spawn_player():
	global p 
	if len(players) < 5:
		player1 = Players(100,5,75)
		players.append(player1)
		p = random.randint(0,3)
		a = random.randint(0,4)
		player1.shape(shapes[a])
		player1.goto(starting_positions[p])

def move_players():
	for player in players:
		player.move()

def check_loss():
	global players
	new_list = []
	for player in players:
		if player.xcor() < 400:
			new_list.append(player)
	players = new_list

def getplayers():
	return players