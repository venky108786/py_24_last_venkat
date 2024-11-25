from operator import truediv
from turtledemo.penrose import start

list_all_int= [1, 2, 6, 5, 8, 4, 3, 52, 46, 3]
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
print("* "*5+"extend"+" *"*5)
s = [1, 2, 3]
s.extend(["hell"])
print(s)
s.extend([2])
print(s)