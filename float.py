import math

def division(y, z):
	return float(z/y)

def addition(a, b):
	c = a+b
	d = ("%.2f" % c)
	return d

def multiplication():
	a = b = c = 2.16
	return (a*b*c)

def subtration(x, y):
	return (x-y)

def ifstate(x, y):
	x = 12.01
	y = 12.001
	if x<=y:
		return y
	else:
		return x 

def elseif(x, y, z):
	if x==y and y==z:
		return x
	elif x==y and z<y:
		return y
	else:
		return z

def forstate():
	n = [float(x)/10 for x in range(10)]
	return n

def whilestate(s, e):
	x = s
	while x<=e:
		return x
		x+=1

def floordiv(n):
	x = n
	y = 4
	z = x // y
	return z

def rectangle(l, w):
	x = l
	y = w
	area = x*y
	float(area)
	z = ("the area of rectangle is %.2f" %area)
	return str(z)

def circle(r):
	y = r
	cir = (math.pi * (y*y))
	float(cir)
	c  = ("circle's area is %.2f cm" %cir)
	return str(c)

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
	i = ("%.2f is the hypotenuse" %z)
	return str(i) 

def cylinder(r, h):
	x = r
	y = h
	a = 2 * (math.pi * (x * y))
	b = 2 * (math.pi *(x * x))
	area = a + b
	z = ("cylinder's area is %.2f" % area)
	return str(z)

def tangent(a, b):
	x=a
	y=b
	tan = (x/y)
	return tan

def parallel(b, h):
	a= b
	c = h
	x = (c*c)
	return x

def trap(a, b, h):
	x = a
	y = b
	z = h
	area = ((x+y)/2) * z
	return area

def square(s):
	x = s
	area = x * x * x * x
	y = ("area of the square %.2f" %area)
	return str(y)

def volume(r, h):
	a = r
	b = h
	vol = math.pi*(a*a)*b
	return vol

def cone(r, h):
	x = r
	y = h
	a = math.pi * x
	b = x + (math.sqrt((y*y) + (x*x)))
	area = a * b
	return str("cone area is %.2f" % area)




print(division(2.5, 16.3))
print(addition(4.5, 6.3))
print(multiplication())
print(subtration(13.45, 6.3))
print(ifstate(12.01, 12.001))
print(elseif(2.01, 2.101, 2.001))
print(forstate())
print(whilestate(1.1, 10.1))
print(floordiv(200.1))
print(rectangle(4, 5.3))
print(circle(17.4))
pyramid(8)
print(triangle(4.2, 6.1))
print(cylinder(5,5.7))
print(tangent(26.0, 15.0))
print(parallel(5.4, 8.1))
print(trap(3.4, 2.8, 10.2))
print(square(3.4))
print(volume(3, 5.5))
print(cone(4.3, 7))
