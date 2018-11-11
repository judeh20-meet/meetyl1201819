import tkinter as tk
from tkinter import simpledialog


'''
greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
if greeting in ("Arrr!"):
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")
'''


'''
# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).


year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
	print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
'''


'''
# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

class Person(object):
	def __init__(self, first_name, last_name):
	    self.first = first_name
	    self.last = last_name
	def speak(self):
  	    print("My name is " + self.first + ", " + self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")
me.speak()
you.speak()
'''
'''
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average    Grade
# 90+    A
# 80-89    B
# 70-79    C
# 60-69    D
# 0-59    F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(simpledialog.askstring("Input", "Input exam grade one: ", parent=tk.Tk().withdraw()))

exam_two = int(simpledialog.askstring("Input", "Input exam grade two: ", parent=tk.Tk().withdraw()))

exam_three = int(simpledialog.askstring("Input", "Input exam grade three: ", parent=tk.Tk().withdraw()))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"
number = 1
for grade in grades:
    print("Exam" + str(number) + ":"   + str(grade))
    number += 1
print("Average: " + str(avg))
print("Letter grade:" + str(letter_grade))
if letter_grade is "F":
    print("Student is failing.")
else:
    print("Student is passing.")
'''

'''
class Person(object):
   def __init__(self, name, favorite_food, age, favourite_color):
       self.name = name
       self.favorite_food = favorite_food
       self.age = age
       self.favourite_color = favourite_color


   def define_color(self, color):
       print("My skin color is " + color + "!")

   def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.favorite_food + " and my favorite color is " + self.favourite_color)


a = Person("Britney", "Pizza", 16, "Blue")
a.print_info()
a.define_color("Black")
b = Person("Jake", "Burgers", 15, "Green")
b.print_info()
b.define_color("White")
'''
'''
class Bear():
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print("Hi! I’m a bear. My name is " + self.name)

my_bear = Bear("Danny")
print("A new bear is created. Its name is: " + my_bear.name)
my_bear.say_hi()
'''