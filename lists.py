def add():
	cars = ["Toyota", "Suzuki", "Honda"]
	cars.append("Ford")
	cars.sort()
	print(cars)

def remove():
	cars = ["Ford", "Honda", "Suzuki", "Toyota"]
	print("Before removing" + str(cars))
	cars.remove("Honda")
	print("After removing" + str(cars))

def update():
	cars = {"Ford", "Honda", "Suzuki", "Toyota"}
	cars.update(["Pajero", "Mitzubishi"])
	sorted(cars)
	print(cars)

def getvalue():
	num = [1, 2, 3, 4 ,5]
	print(num.index(4))

def popval():
	letters = ['a', 'b', 'c', 'd']
	letters.pop()
	print(letters)

def reversing():
	x = [2, 4, 6, 8]
	x.reverse()
	print(x)


def counting():
	x = [1, 2, 3, 4, 5, 6, 7, 8]
	i = 0
	for j in x:
		i+=1
	print(i)

def deletingval():
	city = ["Davao", "Cebu", "Manila", "Butuan"]
	del city[3]
	print(city)

def looping():
	year = [1999, 2000, 2001, 2002, 2003]
	for x in year:
		print(x)

def check():
	year = [1999, 2000, 2001, 2002, 2003]
	if 2001 in year:
		print("Found!")	

def length():
	n = [1, 2, 3, 4, 5, 6]
	print("The length of the list is " + str(len(n)))

def multipleset():
	n = [((1, 2), (3,4)),(1, 2, 3)]
	print(n)
	y = n[0]
	print(y)
	x = y[0]
	print(x)
	z = x[1]
	print(z)

def intersections():
	a = {"a", "b", "c", "d"}
	b = {"a", "d", "f"}
	a.intersection_update(b)
	print(a)

def differences():
	a = {"a", "b", "c", "d"}
	b = {"a", "d", "f"}
	c = b.difference(a)
	print(c)

def symmetric():
	a = {"a", "b", "c", "d"}
	b = {"a", "d", "f"}
	c = a.symmetric_difference(b)
	sorted(c)
	print(c)

def unions():
	a = {1, 2, 3}
	b = {4, 5, 6}
	c = {7, 8, 9}
	d = {10, 11, 12}
	e = a.union(b, c, d)
	print(e)

def extends():
	b = ["True", "False"]
	a = [1, 0]
	b.extend(a)
	print(b)

def whileloop():
	a = [1, 2, 3, 4, 5]
	i = 0
	while i<5:
		i+=2
		print(i)

def sorting():
	x = [8, 4, 5, 6]
	x.append(7)
	x.sort()
	print(x)

def forloop():
	a = [1, 2, 3, 4]
	i = 0
	for i in a:
		print(i)
		i+=1	










add()
remove()
update()
getvalue()
popval()
reversing()
counting()
deletingval()
looping()
check()
length()
multipleset()
intersections()
differences() 
symmetric()
unions()
extends()
whileloop()
sorting()
forloop()