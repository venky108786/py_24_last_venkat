from operator import truediv
from turtledemo.penrose import start

list_all_int= [1, 2, 6, 5, 8, 4, 3, 52, 46, 3,'hi']
list_all_int_1=list_all_int.copy()
#append() int in int
print(list_all_int)
#append() int in str
list_all_int.append("venky") #.append() idhi manam ichhina item ni end of the list lo add chestundhi and it take only single arg
print(list_all_int)
#append() int in float
list_all_int.append(4.8)
print(list_all_int)
#append() int in boolean
list_all_int.append(True)
print(list_all_int)
print("* "*5+"clear method"+" *"*5)
print(list_all_int.clear()) # .clear() method list lo vunna items ni clear chesi "none" return chestundhi
print(list_all_int) # after using clear method print list it gives '[]' like this
print("* "*5+"copy"+" *"*5)
print(list_all_int_1)
print("* "*5+"count"+" *"*5)
print(list_all_int_1.count(7)) #list lo leni item iste adhi zero return chestundi
print(list_all_int_1.count(3))
print(list_all_int_1.count('hi'))

print("* "*5+"extend"+" *"*5)
s=[1,2,3]
print(s.extend([5]))
list_all_int_1.extend(['hello'])
print(list_all_int_1)
print("* "*5+"index"+" *"*5)
print(list_all_int_1.index(3,7))
print(list_all_int_1.index(52))
print(list_all_int_1.index("hello"))
# index() method manam ichhina value okk position ni return chestund
# and() lo starting value and next which position to start ani kuda cheppavachhu
print("* "*5+"insert"+" *"*5)
list_all_int_1.insert(0,5)
print(list_all_int_1)
list_all_int_1.insert(3,'python')
print(list_all_int_1)
list_all_int_1.insert(2,[2,3,5])
print(list_all_int_1)
print("* "*5+"pop"+" *"*5) #Removes the element at the specified position
print(list_all_int_1.pop(2))
print(list_all_int_1)
x=list_all_int_1.pop(3)
print(list_all_int_1)
print(x)
print("* "*5+"remove"+" *"*5) # remove element at specific value
list_all_int_1.remove(2)
print(list_all_int_1)
list_all_int_1.remove(5)
print(list_all_int_1)
print("* "*5+"reverse"+" *"*5)
list_all_int_1.reverse()
print(list_all_int_1)
print("* "*5+"sort"+" *"*5)
l=[1,2,3,5,84,62,25,15,3,25,3,3,56,6,5,6]
l.sort()
print(l)
l.sort(reverse=True)
print(l)