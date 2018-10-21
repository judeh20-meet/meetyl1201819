a = [1,1,2,3,5,8,13,21,34,55,89,7,21,10,]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,89]


def c():
	list3 = []
	
	for i in a:
		if i in b:
			list3.append(i)
		
	return list3
print(c())
