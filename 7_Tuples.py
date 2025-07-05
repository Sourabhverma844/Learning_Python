emp_data = ("Sourabh",80000,172.5)

# lets create an empty tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

#tuple print ho jaega
print(emp_data) 

#tuple me index 1 par jo bhi value he wo print ho jaegi
print(emp_data[1])

#datatype print ho jaega
print(type(emp_data)) 

# emp_data[1] = 30 ye allowed nahi he  kyoki tuples immutable hote he 

# if you create tuple with single value it will not create a tuple rather it create a int
a = (10)
print(type(a))

b = ("z")
print(type(b))
# single element ka tuple banane ke lie , ka use karenge
c = (20,)
print(type(c))

d = ("z",)
print(type(d))

"""we can also create tuples without small parenthesis()"""
sip = 100,200,300,400,700,500,800,600,300
print(sip[2])
print(sip[-1])
print(sip[1:3]) # 1 include 3 exclude

# len gives us length of tuple
print(len(sip))
# count gives us count how many times a value come in tuple
print(sip.count(300))
# index gives us index of element from tuple
print(sip.index(700))

# so many functionality in tuples is like list like max item & min item but functionality which modify the list like reverse, clear and sort are not available, also not have functions to insert and remove item