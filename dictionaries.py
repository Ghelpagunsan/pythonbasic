def show():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao"
	}
	return str(d)

def access():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao"
	}
	x = d.get("age")
	y = d["name"]
	return str(str(y) + " , " + str(x))

def change():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao"
	}
	x = d["city"] = "Bislig"
	return str(x)

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
		return str("Found!")

def add():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao"
	}
	d["status"] = "Single"
	return str(d)

def length():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	return str(len(d))

def remove():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	d.pop("status")
	return str(d)

def updates():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	d.update({"name":"Ghelo"}) 
	return str(d)

def create(x, y):
	d = dict.fromkeys(x)
	return str(d)

def keys():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.keys()
	return str(x)

def default():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.setdefault("age", 19)
	return str(x)

def clearing():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.clear()
	return str(x)

def delete():
	d = {
	"breed" : "Pug",
	"weight" : 15 ,
	"gender" : "Male"
	}
	del d["weight"]
	return str(d)

def dictionary():
	d = dict(a=1, b=2, c=3)
	return str(d)

def copies():
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.copy()
	return str(x)

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
	return str(x)

def setdefaults(): #other way around
	d = {
	"name" : "Gelo",
	"age" : 20 ,
	"city" : "Davao",
	"status" : "Single"
	}
	x = d.setdefault("religion", "Christian")
	return str(x)




print(show())
print(access())
print(change())
getvals()
forloop()
print(check())
print(add())
print(length())
print(remove())
print(updates())
print(create(("Name", "Age", "City"), 0))
print(keys())
print(default())
print(clearing())
print(delete())
print(dictionary())
print(copies())
onebyone()
print(popitems())
print(setdefaults())

