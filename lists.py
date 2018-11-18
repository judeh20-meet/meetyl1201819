list1 = ['1','2','3','4','5']
list2 = ['a','b','c','d','e']
list3 = []


for i in range(len(list1 + list2)):
	if i % 2 == 0:
		list3.append(i)
	if i % 2 == 1:
		list3.append(i)

print(list3)
