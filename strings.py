def splitting(x):
	print(x.split(" "))

def concatenate(n):
	x = "Holy"
	print(str(x) + str(n))

def length(n):
	print(len(n))

def position(n):
	print(n[5])

def whitespace(n):
	print(n.strip())

def lowercasing(n):
	print(n.lower())

def uppercasing(n):
	print(n.upper())

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
		print("Match")
	else:
		print("Unmatch")

def elifstate(n):
	n = len(n)
	x = len("perfect")
	if x == n:
		print("Match")
	elif n<x:
		print("Add more")
	else:
		print("Unmatch")

def range(n):
	print(n[3:6])

def names():
	n = ["Joy", "Shem", "Van", "Mark"]
	for x in n:
		print(x)

def numbering():
	n = ["hi", "hello", "go"]
	for a, b in enumerate(n):
		print(a, b)

def replacing(n):
	print(n.replace("n", "m"))

def check():
	n = ["hi", 5, "me", 4]
	if  "hi" in n:
		print("Existing")
	else:
		print("add!")

def counting():
	n = ["hi", 5, 5, 5, "hello"]
	print(n.count(5))

def inttostr(n):
	print(str(n))

def adding():
	a = "Hello"
	b = "Hi"
	c = a + b
	print(len(c))

def subtracting():
	a = "molten"
	b = "grab"
	x = len(a)
	y = len(b)
	c = x - y
	print(c)






splitting("2 5 3 5")
concatenate("Cross")
length("qwertyuiop")
position("trinity")
whitespace("Call maybe")
lowercasing("AMAZING")
uppercasing("good job")
forlooping("Morning")
whilelooping("Evening")
ifstate("seven")
elifstate("torment")
range("moment")
names()
numbering()
replacing("nick")
check()
counting()
inttostr(234)
adding()
subtracting()