def show():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao"
	}
	print(d)

def access():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao"
	}
	x = d.get("age")
	y = d["name"]
	print(str(y) + " , " + str(x))

def change():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao"
	}
	x = d["city"] = "Bislig"
	print(x)

def getvals():
	d = {
	"breed" : "Pug",
	"weight" : 15 ,
	"gender" : "Male"
	}
	for x in d.values():
		print(x)

def forloop(): #using the items()
	d = {
	"breed" : "Pug",
	"weight" : 15 ,
	"gender" : "Male"
	}
	for x, y in d.items():
		print(x, y)

def check():
	d = {
	"breed" : "Pug",
	"weight" : 15 ,
	"gender" : "Male"
	}
	if "gender" in d:
		print("Found!")

def add():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao"
	}
	d["status"] = "Single"
	print(d)

def length():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	print(len(d))

def remove():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	d.pop("status")
	print(d)

def updates():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	d.update({"name":"Ghelo"}) 
	print(d)

def create():
	x = ("Name", "Age", "City")
	y= (0)
	d = dict.fromkeys(x)
	print(d)

def keys():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.keys()
	print(x)

def default():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.setdefault("age", 19)
	print(x)

def clearing():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.clear()
	print(x)

def delete():
	d = {
	"breed" : "Pug",
	"weight" : 15 ,
	"gender" : "Male"
	}
	del d["weight"]
	print(d)

def dictionary():
	d = dict(a=1, b=2, c=3)
	print(d)

def copies():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.copy()
	print(x)

def onebyone():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	for x in d:
		print(d[x])

def popitems(): #retieve the popped key and value
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.popitem()
	print(x)

def setdefaults(): #other way around
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.setdefault("religion", "Christian")
	print(x)




show()
access()
change()
getvals()
forloop()
check()
add()
length()
remove()
updates()
create()
keys()
default()
clearing()
delete()
dictionary()
copies()
onebyone()
popitems()
setdefaults()

