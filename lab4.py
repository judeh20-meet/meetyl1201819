class Animal(object):
	
	def __init__(self, sound, name, age, favourite_color):
		self.sound = sound
		self.name = name
		self.age = age 
		self.favourite_color = favourite_color
	def eat(self,food):
		print("Yummy!! " + self.name + " is eating " + food)
	def make_sound(self,number):
		print(self.name + " says " + self.sound * number)
	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favourite_color)
dog = Animal("Bork", "Doggy", "2", "gray")
dog.eat("meat")
dog.description()
dog.make_sound(6)