from turtle import *
import turtle
import random
import time
from Player import *


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
start_pos1 = (-800,375)
starting_positions.append(start_pos1)
start_pos2 = (-800,155)
starting_positions.append(start_pos2)
start_pos3 = (-800,-65)
starting_positions.append(start_pos3)
start_pos4 = (-800,-275)
starting_positions.append(start_pos4)


class Players(Turtle):
	def __init__(self,dx,dy):
		Turtle.__init__(self, visible = False)
		self.dx = dx
		self.dy = dy
		self.penup()
		self.shapesize(1)
		self.speed(0)
	
	def move(self):
		self.speed(1)
		self.forward(50)


players = []

			

def spawn_player():
	if len(players) < 5:
		player1 = Players(100,5)
		players.append(player1)
		p = random.randint(0,3)
		a = random.randint(0,4)
		player1.shape(shapes[a])
		player1.goto(starting_positions[p])

def move_players():
	for player in players:
		player.showturtle()
		player.move()

def check_loss():
	global players
	new_list = []
	for player in players:
		if player.xcor() < 400:
			new_list.append(player)
	players = new_list



while True:
	spawn_player()
	move_players()
	check_loss()


	

	
	

turtle.mainloop()