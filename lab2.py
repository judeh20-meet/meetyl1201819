import tkinter as tk
from tkinter import simpledialog


'''
a = [1,2,3,4,5]
def newlist():
	b = [a[0],a[-1]]
	print(b)
newlist()
'''


'''
b = []

a = [1,1,2,3,6,56,7,4,78,90]
for i in a:
	if i < 5:
		b.append(i)
print(b)
'''


'''
a = [1,1,2,3,5,8,13,21,34,55,89,7,21,10,]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,89]


def c():
	list3 = []
	
	for i in a:
		if i in b:
			list3.append(i)
		
	return list3
print(c())
'''



'''
print("Welcome! I am the prime number magician!")
number = simpledialog.askstring("HI", "Tell me a number and i will tell you if it is Prime or not", parent=tk.Tk().withdraw())

for i in range(1):
	if int(number) == 2:
		print("Your number is Prime") 
		quit()
	if int(number) % 2 == 0:
		print("Your number is not Prime!")
	else:
		print("Your number is Prime") 
'''