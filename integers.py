def add():
	a=5
	b=6
	c=a+b
	return c


def substract(n):
	return 100 - n

def multiply():
	x = 2
	y = 4
	return x*y

def divide(n):
	return 100 / n

def cont(age):
	c = "I am " + str(age) + " years old"
	return c

def greater(a, b):
	if a<b:
		return a
	else:
		return b

def lesser(n):
	a = 15
	b = str("I lose")
	c = str("i Win")
	if a<n:
		return b
	else:
		return c

def recursion(n):
	if n<=20:
		return n
	else:
		return n * recursion(n+1)

def equal(n):
	a = 21
	if a==n:
		return str("Match")
	else:
		return str("Nah")

def forloop():
	sum = [1,2,3,4]
	for i in sum:
		return sum

def whileloop():
	i = 2
	while i<6:
		return i
		i+=1

def ifstate():
	a = 3
	b = 5
	if a<=b:
		return str("Yey")
	else:
		return str("Nay")

def elifstate(a, b):
	if a<b:
		return a+b
	elif a>b:
		return a-b
	else:
		return a*b

def swap(a, b):
	c = str("Before swap a = %d and b = %d" %(a, b))
	a, b = b, a
	d = str("After swaping a = %d and b = %d" %(a, b))
	return str(c + "\n" + d)

def insert(sum):
	#sum = [1,2,3]
	sum.insert(3, 4)
	a = sum[3]
	return a

def popnum():
	x = [2,4,6,8]
	x.pop()
	return x

def triangle(n):
    x = 1
    while (x <= n):
        print("1" * x)
        x = x + 1
    return

def count(xam):
	#xam = [1,1,1,2,2]
	f=0
	l=0
	for i in xam:
		if i==1:
			f+=1
		elif i==2:
			l+=1
	a = str("number of one found %d" %f)
	b = str("number of two found %d" %l)
	return str(a + "\n" + b)

def plainprint():
	a = b = c = 6
	return b
	

def convert(num):
	i = int(num)
	return i 



print(substract(50))
print(add())
print(multiply())
print(int(divide(2)))
print(cont(20))
print(greater(5, 6))
print(lesser(20))
print(int(recursion(20)))
print(equal(21))
print(forloop())
print(whileloop())
print(ifstate())
print(elifstate(4, 5))
print(swap(3,5))
print(insert([1,2,3]))
print(popnum())
triangle(6)
print(count([1,1,1,2,2]))
print(plainprint())
print(convert("123456"))