def check(n):
	x = n
	return(bool(x%2==0))

def notequal():
	x=10
	y=9
	return(bool(x==y))

def array():
	x = [1,2,3]
	return(bool(x))

def add():
	x = 8
	y = 3
	z = x + y
	if z == 11:
		return str("8+3 is 11 " + str(bool(z)))
	else:
		return str("False")

def sub(a, b):
	x = a
	y = b
	z = x - b
	if z < 0:
		return("Negative!" + str(bool(z)))
	else:
		return("Positive!" + str(bool(z)))

def prod(a, b):
	z = a * b
	if bool(z%10==0):
		return True
	elif bool(z%10!=0):
		return False

def quo(a, b):
	c = a/b
	d = 5
	if c == 5:
		return bool(c==d)
	else:
		return bool(c==d)

def ifst(a, b):
	if a>b:
		return bool(a>b)
	else:
		return bool(a>b)

def elifst():
	x = y  = 13
	#x =13
	#y=4
	if x < y:
		return bool(x<y)
	elif x == y:
		return bool(x==y)
	else:
		return bool(x>y)

def none():
	a = None
	return bool(a)

def string():
	x = "Go"
	y = x, 'is', bool(x)
	return str(y)

def integer(n):
	return bool(n)

def whileloop(n):
	while True:
		if n == 4:
			return True
			break
		else:
			return False
			break

def expression():
	a = 5
	b = 8
	x = (4, not a == 8 and b == 8)
	return str(x)

def mapping():
	map = {}
	return bool(map)

def forloop(arr):
	a = 0
	for i in arr:
		return bool(i)
		a+=1

def float(n):
	return bool(n)

def boolean():
	variable = False
	if variable == True:
	    return str("The function is True!")
	else:
	    return str("The function is False.")


def andstate(x):
	boolean = True
	y = ((x>=5) and (boolean==True))
	return y

def orstate(a):
	boolean = False
	b = ((a<6) or (boolean==False))
	return b






#-----------------------------------------------#

x = 4
if (check(x)):
		print("Even Number-True")
else:
	print("Odd Number-False")

print(notequal())
print(array())
print(add())
print(sub(5, 2))
print(prod(5, 4))
print(quo(10, 4))
print(ifst(5, 3))
print(elifst())
print(none())
print(string())
print(integer(0))
print(whileloop(4))
print(expression())
print(mapping())
print(forloop([1]))
print(float(0.0))
print(boolean())
print(andstate(3))
print(orstate(4))