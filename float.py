import math

def division():
	y = 5.02
	z = 15.13
	print(z/y)

def addition():
	a = 1.1
	b = 2.16
	c = a+b
	print("%.2f" % c)

def multiplication():
	a = b = c = 2.16
	print(a*b*c)

def subtration():
	x = 12.01
	y = 4.88
	print(x-y)

def ifstate():
	x = 12.01
	y = 12.001
	if x<=y:
		print(y)
	else:
		print(x)

def elseif():
	x=2.1
	y=2.101
	z=2.01
	if x==y and y==z:
		print(x)
	elif x==y and z<y:
		print(y)
	else:
		print(z)

def forstate():
	n = [float(x)/10 for x in range(10)]
	print(n)

def whilestate(s, e):
	x = s
	while x<=e:
		print(x)
		x+=1

def floordiv(n):
	x = n
	y = 4
	z = x // y
	print(z)

def rectangle(l, w):
	x = l
	y = w
	area = x*y
	float(area)
	print("the area of rectangle is %.2f" %area)

def circle(r):
	y = r
	cir = (math.pi * (y*y))
	float(cir)
	print("circle's area is %.2f cm" %cir)





division()
addition()
multiplication()
subtration()
ifstate()
elseif()
forstate()
whilestate(1.1, 10.1)
floordiv(200.1)
rectangle(4, 5.3)
circle(17.4)