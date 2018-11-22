def add():
	cars = ["Toyota", "Suzuki", "Honda"]
	cars.append("Ford")
	cars.sort()
	return cars

def remove():
	cars = ["Ford", "Honda", "Suzuki", "Toyota"]
	print("Before removing" + str(cars))
	cars.remove("Honda")
	return str("After removing" + str(cars))

def update():
	cars = {"Ford", "Honda", "Suzuki", "Toyota"}
	cars.update(["Pajero", "Mitzubishi"])
	sorted(cars)
	return cars

def getvalue(num):
	return str(num.index(4))

def popval(letters):
	letters.pop()
	return letters

def reversing(x):
	x.reverse()
	return x


def counting(x):
	i = 0
	for j in x:
		i+=1
	return i

def deletingval(city):
	del city[3]
	return city

def looping():
	year = [1999, 2000, 2001, 2002, 2003]
	for x in year:
		print(x)

def check():
	year = [1999, 2000, 2001, 2002, 2003]
	if 2001 in year:
		return str("Found!")	

def length(n):
	return str("The length of the list is " + str(len(n)))

def multipleset():
	n = [((1, 2), (3,4)),(1, 2, 3)]
	return str(n)
	y = n[0]
	return str(y)
	x = y[0]
	return str(x)
	z = x[1]
	return str(z)

def intersections(a, b):
	a.intersection_update(b)
	return str(a)

def differences(a, b):
	c = b.difference(a)
	return str(c)

def symmetric(a, b):
	c = a.symmetric_difference(b)
	sorted(c)
	return str(c)

def unions():
	a = {1, 2, 3}
	b = {4, 5, 6}
	c = {7, 8, 9}
	d = {10, 11, 12}
	e = a.union(b, c, d)
	return str(e)

def extends():
	b = ["True", "False"]
	a = [1, 0]
	b.extend(a)
	return str(b)

def whileloop():
	a = [1, 2, 3, 4, 5]
	i = 0
	while i<5:
		i+=2
		print(i)

def sorting(x):
	x.append(7)
	x.sort()
	return str(x)

def forloop():
	a = [1, 2, 3, 4]
	i = 0
	for i in a:
		print(i)
		i+=1	










print(add())
print(remove())
print(update())
print(getvalue([1, 2, 3, 4 ,5]))
print(popval(['a', 'b', 'c', 'd']))
print(reversing([2, 4, 6, 8]))
print(counting([1, 2, 3, 4, 5, 6, 7, 8]))
print(deletingval(["Davao", "Cebu", "Manila", "Butuan"]))
looping()
print(check())
print(length([1, 2, 3, 4, 5, 6]))
print(multipleset())
print(intersections({"a", "b", "c", "d"}, {"a", "d", "f"}))
print(differences({"a", "b", "c", "d"}, {"a", "d", "f"})) 
print(symmetric({"a", "b", "c", "d"}, {"a", "d", "f"}))
print(unions())
print(extends())
whileloop()
print(sorting([8, 4, 5, 6]))
forloop()