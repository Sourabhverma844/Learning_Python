# id() in python

print(id(5))

a = 10
print(id(a))

b = a
print(id(b))

###############################################

w = 100
x = 100
print(id(w))
print(id(x))

y = "Sourabh"
z = "Sourabh"
print(id(y))
print(id(z))

###############################################

# if two variable has same id it means they are refer to same object 
# we use is operator two check if the identities of two operants are same or not

m = 50
n = 50
print(m is n)
o = m
print(o is n)
o = 20
print(o is n)

###############################################

e = 11
f = 11.5
g  = 2+4j
h = True
i = None
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

###############################################

emp_name = "Sourabh"
print(type(emp_name))

cars = ["Verna","Honda City","Thar"]
print(type(cars))

sip = (1000,2000,3000)
print(type(sip))

earnings = {50000,30000,45000}
print(type(earnings))

sources = {50000:"ripple",30000:"YouTube",45000:"Promotions"}
print(type(sources))
