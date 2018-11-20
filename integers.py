def add():
	a=5
	b=6
	c=a+b
	print(c)


def substract(n):
	return 100 - n

def multiply():
	x = 2
	y = 4
	print(x*y)

def divide(n):
	return 100 / n

def cont(age):
	print("I am " + str(age) + " years old")

def greater():
	a = 3
	b = 4
	if a<b:
		print("A")
	else:
		print("B")

def lesser(n):
	a = 15
	if a<n:
		print("I Lose")
	else:
		print("I Win")

def recursion(n):
	if n<=20:
		return n
	else:
		return n * recursion(n+1)

def equal(n):
	a = 21
	if a==n:
		print("Match")
	else:
		print("Nah")

def forloop():
	sum = [1,2,3,4]
	for i in sum:
		print(sum)

def whileloop():
	i = 2
	while i<6:
		print(i)
		i+=1

def ifstate():
	a = 3
	b = 5
	if a<=b:
		print("Yey")
	else:
		print("Nay")

def elifstate():
	a = 3
	b = 4
	if a<b:
		print(a+b)
	elif a>b:
		print(a-b)
	else:
		print(a*b)

def swap():
	a = 1
	b = 2
	print("Before swap a = %d and b = %d" %(a, b))
	a, b = b, a
	print("After swaping a = %d and b = %d" %(a, b))

def insert():
	sum = [1,2,3]
	sum.insert(3, 4)
	print(sum[3])

def popnum():
	x = [2,4,6,8]
	x.pop()
	print(x)

def triangle(n):
    x = 1
    while (x <= n):
        print("1" * x)
        x = x + 1
    return

def count():
	xam = [1,1,1,2,2]
	f=0
	l=0
	for i in xam:
		if i==1:
			f+=1
		elif i==2:
			l+=1
	print("number of one found %d" %f)
	print("number of two found %d" %l)

def plainprint():
	a = b = c = 5
	print(a,b,c)

def iterate():
	num = "123456789"
	it = iter(num)

	print(int(next(it)))
	print(int(next(it)))
	print(int(next(it)))
	print(int(next(it)))
	print(int(next(it)))
	print(int(next(it)))
	print(int(next(it)))
	print(int(next(it)))
	print(int(next(it)))




print(substract(50))
add()
multiply()
print(int(divide(2)))
cont(20)
greater()
lesser(20)
print(int(recursion(20)))
equal(21)
forloop()
whileloop()
ifstate()
elifstate()
swap()
insert()
popnum()
triangle(6)
count()
plainprint()
iterate()