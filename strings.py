def splitting(x):
	return str(x.split(" "))

def concatenate(n):
	x = "Holy"
	y = (str(x) + str(n))
	return y

def length(n):
	m = len(n)
	return m

def position(n):
	return str(n[5])

def whitespace(n):
	return n.strip()

def lowercasing(n):
	return str(n.lower())

def uppercasing(n):
	return str(n.upper())

def forlooping(n):
	for i in n:
		print(i)

def whilelooping(n):
	x= len(n) - 1
	while x >= 0:
		print(n[x])
		x-=1

def ifstate(n):
	n = len(n)
	x = len("perfect")
	if x == n:
		return str("Match")
	else:
		return str("Unmatch")

def elifstate(n):
	n = len(n)
	x = len("perfect")
	if x == n:
		return str("Match")
	elif n<x:
		return str("Add more")
	else:
		return str("Unmatch")

def range(n):
	return str(n[3:6])

def names():
	n = ["Joy", "Shem", "Van", "Mark"]
	for x in n:
		print(x)

def numbering():
	n = ["hi", "hello", "go"]
	for a, b in enumerate(n):
		print(a, b)

def replacing(n):
	x = (n.replace("n", "m"))
	return x

def check():
	n = ["hi", 5, "me", 4]
	if  "hi" in n:
		return str("Existing")
	else:
		return str("add!")

def counting():
	n = ["hi", 5, 5, 5, "hello"]
	x = (n.count(5))
	return x

def inttostr(n):
	return str(n)

def adding():
	a = "Hello"
	b = "Hi"
	c = a + b
	return str(len(c))

def subtracting():
	a = "molten"
	b = "grab"
	x = len(a)
	y = len(b)
	c = x - y
	return str(c)






print(splitting("2 5 3 5"))
print(concatenate("Cross"))
print(length("qwertyuiop"))
print(position("trinity"))
print(whitespace("Call maybe"))
print(lowercasing("AMAZING"))
print(uppercasing("good job"))
forlooping("Morning")
whilelooping("Evening")
print(ifstate("seven"))
print(elifstate("torment"))
print(range("moment"))
names()
numbering()
print(replacing("nick"))
print(check())
print(counting())
print(inttostr(234))
print(adding())
print(subtracting())