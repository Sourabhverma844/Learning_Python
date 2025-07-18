# lets create an empty list
empty_list = []
print(empty_list)
print(type(empty_list))

weights = [50,60,70,80,90]
print(weights)

print(weights[0])
print(weights[2])
print(weights[4])
print(weights[-2])
print(weights[-4])

###############################################

"""we use list.append(element) to add element in list, this element is added in the end of list """
weights.append(20)
print(weights) 

"""we use list.insert(index,element) to insert element on given index"""
weights.insert(1,10)
print(weights)

"""element in list returns us true if element is present in list and false if not"""
print(50 in weights)

"""list.count(element) gives us the number that how many times the given element is occur in list"""
print(weights.count(60))

"""list.index(element) gives us the index no. of element from list"""
print(weights.index(80))
print(weights)

"""list.index(element,index_inclusive,index_exclusive) so this function start searching value between this indexes and return us the index no of that value and if element is not exists it throws a ValueError"""
print(weights.index(50,0,7))

##############################################

print(weights)

"""list.remove(element) removes the element from list and returns none"""
print(weights.remove(70)) 
print(weights)

"""list.pop() removes the last element from list and return that element
we can also provide index no of the value that we want to remove list.pop(index )
"""
print(weights.pop())
print(weights.pop(2))
print(weights)

"""del list[index] removes the item from list we cam also provide the range of index so all the elements will be removed from the list del list[inclusive_index : exclusive_index]"""
del weights[1]
print(weights)
del weights[0:2]
print(weights)

###############################################

age = [33,77,11,44,22,66,55,88]
print(age)

"""max(list) return us the matahamatically max value from the list"""
print(max(age))

"""min(list) return us the matahamatically min value from the list"""
print(min(age))

"""sum(list) return us the sum of all values from the list"""
print(sum(age))

"""list.reverse() reverse the whole list and retuns none"""
age.reverse()
print(age)

"""list.sort() sorted the whole list in increasing order and return none"""
age.sort()
print(age)

"""remember this all functions max,min,sum,reverse,sort is only works on the list that have all of its element as number
for examp : we can not use this functions on list with elements  [10,20,"Sourabh",30]"""

"""["abc","def","gfg"] is all of the elements are strings then max,min,sum,sort will work and gives us ans lexiographically but sum() not works"""