def check(n):
	x = n
	return(bool(x%2==0))

def notequal():
	x=10
	y=9
	print(bool(x==y))

def array():
	x = [1,2,3]
	print(bool(x))

def add():
	x = 8
	y = 3
	z = x + y
	if z == 11:
		print("8+3 is 11 " + str(bool(z)))
	else:
		print("False")

def sub(a, b):
	x = a
	y = b
	z = x - b
	if z < 0:
		print("Negative!" + str(bool(z)))
	else:
		print("Positive!" + str(bool(z)))

def prod(a, b):
	z = a * b
	if bool(z%10==0):
		print("True")
	elif bool(z%10!=0):
		print("False")

def quo():
	a = 10
	b = 4
	c = a/b
	d = 5
	if c == 5:
		print(bool(c==d))
	else:
		print(bool(c==d))

def ifst():
	a = 5
	b = 3
	if a>b:
		print(bool(a>b))
	else:
		print(bool(a>b))

def elifst():
	x = y  = 13
	#x =13
	#y=4
	if x < y:
		print(bool(x<y))
	elif x == y:
		print(bool(x==y))
	else:
		print(bool(x>y))

def none():
	a = None
	print(bool(a))

def string():
	x = "Go"
	print(x, 'is', bool(x))

def integer(n):
	print(bool(n))

def whileloop(n):
	while True:
		if n == 4:
			print("True")
			break
		else:
			print("False")
			break

def expression():
	a = 5
	b = 8
	print(4, not a == 8 and b == 8)

def mapping():
	map = {}
	print(bool(map))

def forloop():
	arr=[1]
	a = 0
	for i in arr:
		print(bool(i))
		a+=1

def float(n):
	print(bool(n))

def boolean():
	variable = False
	if variable == True:
	    print("The function is True!")
	else:
	    print("The function is False.")


def andstate():
	x = 3
	boolean = True
	print((x>5) and (boolean==True))

def orstate():
	a = 6
	boolean = False
	print((a<6) or (boolean==False))






#-----------------------------------------------#

x = 4
if (check(x)):
		print("Even Number-True")
else:
	print("Odd Number-False")

notequal()
array()
add()
sub(5, 2)
prod(5, 4)
quo()
ifst()
elifst()
none()
string()
integer(0)
whileloop(4)
expression()
mapping()
forloop()
float(0.0)
boolean()
andstate()
orstate()