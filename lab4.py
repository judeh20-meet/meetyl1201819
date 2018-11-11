
'''
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
'''

class Person(object):

	def __init__(self, name, age, city, gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat_breakfast(self,food):
		print(self.name + " is eating his favourite breakfast!" + food)
	def visit_parent(self,parent):
		print(self.name + " went to visit his dad, " + parent + "!")

person1 = Person("Bob", 27, "Moscow", "male")
person1.eat_breakfast(" Green eggs and ham!")
person2 = Person("Jimmy", 27, "Egypt", "male")
person2.eat_breakfast(" Corn flakes!")
person1.visit_parent("Jimmy")
person2.visit_parent("Henry")
