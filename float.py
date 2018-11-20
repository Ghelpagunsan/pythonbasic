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

def pyramid(n):
    x = 1
    while (x <= n):
        print("1.01" * x)
        x = x + 1
    return

def triangle(a, b):
	x = a * a
	y = b * b
	z = math.sqrt(x+y)
	print("%.2f is the hypotenuse" %z) 

def cylinder(r, h):
	x = r
	y = h
	a = 2 * (math.pi * (x * y))
	b = 2 * (math.pi *(x * x))
	area = a + b
	print("cylinder's area is %.2f" % area)

def tangent(a, b):
	x=a
	y=b
	tan = (x/y)
	print(tan)

def parallel(b, h):
	a= b
	c = h
	print(c*c)

def trap(a, b, h):
	x = a
	y = b
	z = h
	area = ((x+y)/2) * z
	print (area)

def square(s):
	x = s
	area = x * x * x * x
	print("area of the square %.2f" %area)

def volume(r, h):
	a = r
	b = h
	vol = math.pi*(a*a)*b
	print(vol)

def cone(r, h):
	x = r
	y = h
	a = math.pi * x
	b = x + (math.sqrt((y*y) + (x*x)))
	area = a * b
	print("cone area is %.2f" % area)




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
pyramid(8)
triangle(4.2, 6.1)
cylinder(5,5.7)
tangent(26.0, 15.0)
parallel(5.4, 8.1)
trap(3.4, 2.8, 10.2)
square(3.4)
volume(3, 5.5)
cone(4.3, 7)
