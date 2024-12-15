
from re import split
#1.Write a Python program to count the number of vowels in a given string.
s="aeiousfwersfsggakdsjgklajw4e5w544!@#%#$^aefg"
vowels=["A","E","I","O","U"]
vowels_in_str=[]
count=0
for i in s:
    if i.upper() in vowels:
        vowels_in_str.append(i)
        count+=1
print(count)

#2.Reverse the string "Python is fun!" without using slicing.
given_str="Python is fun!"
conv_str_list=list(given_str)
conv_str_list.reverse()
print(conv_str_list)
result_reverse=''
for i in conv_str_list:
    result_reverse+=i
print(result_reverse)

#3.Check if the string "madam" is a palindrome.
given_pli="madam"
rever_pali=given_pli[::-1]
check_pali_or_not=given_pli==rever_pali
if check_pali_or_not:
    print("it is polindram")
else:
    print("it is not polindram")

#4.Find and replace the word "Python" with "Programming" in the string "I love Python."
given_replce="I love Python."
print(given_replce.replace("Python","Programming"))

#5.Convert the string "hello world" to the title case.
given_title_case= "hello world"
print(given_title_case.title())

#6.Extract all the digits from the string "abc123xyz456".
dig_str="abc123xyz456"
result_only_dig=''
for i in dig_str:
    if i.isdigit():
        result_only_dig+=i
print(result_only_dig)

#7.Join a list of strings ["Python", "is", "awesome"] into a single string separated by spaces.
given_list_str=["Python", "is", "awesome"]
convt_str=''
for i in given_list_str:
    convt_str+=i+" "
print(convt_str)
#/////////////////method 02////////////////////////////
result_of_7=" ".join(given_list_str)
print(result_of_7)

#8.Write a Python program to check if a given string starts with "Hello".
sample_word='Hello everyone'
print(sample_word.startswith("Hello"))
if sample_word.startswith("Hello"):
    print("yes this sentence starts with \"Hello\"")

#9.Count the occurrence of each character in the string "hello".
given_str9="hello"
result_of_9={}
for i in given_str9:
    le_count=given_str9.count(i)
    result_of_9.setdefault(i,le_count)#////learn new thing////:-in dic we can use setdefault() to add key,value
print(result_of_9)

#10.Split the string "apple, banana, cherry" by commas.
given_str_10="apple, banana, cherry"
print(given_str_10.split(","))

#********************************NUMBER************************************

#1.Write a program to check if a given number is prime.
given_num=input("please enter numbers only: ")
if given_num.isnumeric():
    num=int(given_num)
    x1 = False
    for i in range(2,num):
        for j in range(2,i):
            x=(i*j)
            if x==num:
                x1=True
    if x1:
        print("given number is not prime")
    elif num==1:
        print("given number is not prime")
    else:
        print("given number is prime")

#2. Find the greatest common divisor (GCD) of two numbers
gcd_of_two_num_1=int(input("enter gcd1: "))
gcd_of_two_num_2=int(input("enter gcd2: "))
big_num=0
if gcd_of_two_num_1>gcd_of_two_num_2:
    big_num=gcd_of_two_num_1
else:
    big_num=gcd_of_two_num_2
    gcd_li=[]
for i in range(1,big_num+1):
    if gcd_of_two_num_1%i==0 and gcd_of_two_num_2%i==0:
        gcd_li.append(i)
print(f' the GCF of {gcd_of_two_num_1} and {gcd_of_two_num_2} is {gcd_li[-1]}')

#3. Generate a Fibonacci sequence up to 50.
#3. Generate a Fibonacci sequence up to 50.
def fibancci(numm):
    if num==0:
        return []
    elif num==1:
        return [0]
    elif numm==2:
        return [0,1]
    li=[0,1]
    for i in range(2,numm):
        li.append(li[-1]+li[-2])
    return  li

numm=int(input("enter fibanacci: "))
result=fibancci(numm)
print(result)
#4. Convert the decimal number 255 to binary, octal, and hexadecimal.
def con_deci_binary(p):
    if p==0:
        return 0
    binary_code=''
    while p>0:
        r=p%2
        p=p//2
        binary_code=str(r)+binary_code
    return binary_code
def con_deci_octal(n):
    return oct(n)[2:]
def con_deci_hexa(n):
    return hex(n)[2:]

inp=int(input("enter num:" ))
result=con_deci_binary(inp)
result_1=con_deci_octal(inp)
result_2=con_deci_hexa(inp)
print("binary num",result)
print("octal num",result_1)
print("hexadecimal num",result_2)
#5. Calculate the factorial of a number using recursion.

def factorial(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    return num*factorial(num-1)

fact_num=int(input("enter factorial num:"))
result_fac=factorial(fact_num)
print(result_fac)
#6. Check if a number is a perfect square.
check_square_num=int(input("enter square num: "))
numm=0
perfect_square=False
for i in range(check_square_num):
    if i*i==check_square_num:
        perfect_square=True
        numm=i
if perfect_square:
    print(f'{check_square_num} is a perfect square of {numm}')
else:
    print(f'{check_square_num} is not a perfect square')

#7. Determine if a number is even or odd without using the modulus operator.
inp=int(input("enter_odd_even_num:"))
if (inp//2)*2==inp:
    print(f'is a even num{inp}')
else:
    print(f'is a odd num{inp}')
#8. Write a program to reverse the digits of an integer, e.g., 123 -> 321.
given_numb=123
result=int((str(given_numb))[::-1])
print(result)
#9.Round the number 12.34567 to 3 decimal places.
print(round(12.34567,3))

#10Write a program to find the sum of digits of the number 9876.
summ=0
for i in str(9876):
    summ+=int(i)
print(summ)

#/************************List***************************
#************************************************************

#1. Write a Python program to find the largest and smallest numbers in a list
given_list=[5,7,6,2,4,6,8,1,3,4,56,231,77,56,5,22,3]
print(max(given_list))
print(min(given_list))

#2. Remove duplicates from the list [1, 2, 2, 3, 4, 4, 5]

given_li=[1, 2, 2, 3, 4, 4, 5]
con_li_set=set(given_li)
con_set_li=list(con_li_set)
print(con_set_li)

#3. Sort a list of strings alphabetically.

st_inp = input("Enter strings separated by spaces: ").split()
sorted_strings = sorted(st_inp)
print("Sorted strings:", sorted_strings)

#4. Rotate the list [1, 2, 3, 4, 5] one position to the right.

nums = [1, 2, 3, 4, 5]
rot_list = [nums[-1]] + nums[:-1]
print(rot_list)

#5. Merge two lists [1, 2, 3] and [4, 5, 6] without duplicates.
lists1=[1, 2, 3]
lists2=[4, 5, 3]
merged_list=lists1+lists2
print(list(set(merged_list)))

#6. Find the second-largest number in the list [10, 20, 4, 45, 99]
gi=[10, 20, 4, 45, 99]
sorted_list=sorted(gi)
print(sorted_list[-2])

#7. Flatten a nested list [[1, 2], [3, 4], [5]].
li=[[1, 2], [3, 4], [5]]
flatten_list=[]
for i in li:
    flatten_list.extend(i)
print(flatten_list)

#8. Write a Python program to count occurrences of an element in a list.

given_lis=input("given num separated by space: ").split()
count_element=int(input("enter count element: "))
lis=[]
for i in given_lis:
    lis.append(int(i))
count_result=lis.count(count_element)
print(count_result)

#9.Find the intersection of two lists [1, 2, 3] and [2, 3, 4].
lis_1=[1, 2, 3]
lis_2=[2, 3, 4]
intersection_li=list(set(lis_1)&set(lis_2))
print(intersection_li)

#10. Write a Python program to remove all elements from a list that are divisible by 3.
giv_lis=input("enter num separated by space:").split()
x=[int(num) for num in  giv_lis]
result_d3=[i for i in x if i%3!=0]
print(result_d3)


#*******************************************************************
#**************************sets*************************************

#1.Create a set from a list and remove duplicates.

liss=[1,2,3,2,1,6,5,4,5,2,9,8,7,45,21,3,4,11,21,]
set_liss=set(liss)
print(set_liss)
print(list(set_liss))

#2.Write a Python program to find the union of two sets {1, 2, 3} and {3, 4, 5}
set_1={1, 2, 3}
set_2={3, 4, 5}
result_union=set_1.union(set_2)
print(result)

#3. Find the intersection of two sets {1, 2, 3} and {2, 3, 4}.

set_1={1, 2, 3}
set_2={2, 3, 4}
print(set_1 & set_2)
print(set_1.intersection(set_2))

#4. Check if {1, 2} is a subset of {1, 2, 3, 4}.

set_1={1, 2}
set_2={1, 2, 3, 4}
result=set_1.issubset(set_2)
print(result)
print("yes set_1 is subset of set_2")

#5.Remove an element from a set and handle the case if the element is not found.
set_5={1,2,3,True,"nithin"}
result_5=set_5.discard(1)
result_55=set_5.discard(6)
print("after eliminate",set_5)
print(result_55)

#6 Find the difference between two sets {1, 2, 3} and {2, 3, 4}
set_6={1, 2, 3}
set_66={2, 3, 4}
print(set_6-set_66)
result_6=set_6.difference(set_66)
print(result_6)
result_66=set_66.difference(set_6)
print(result_66)

#7. Write a Python program to add multiple elements to a set.
set_big=set()
li=[2,3,"56","nithin",32.3,True,("nithin","venky")]
for i in li:
    set_big.add(i)
print(set_big)

#8. Create a frozen set and demonstrate how it differs from a regular set.

regular_set = {1, 2, 3}
frozen_set = frozenset({1, 2, 3})
print("Regular Set:", regular_set)
print("Frozenset:", frozen_set)

#9.Write a program to find elements that are in either of two sets but not in both
set_9={2,3,4,5,6,True,"nithin"}
set_99={2,3,12,"lalith",False,0}
print(set_99.symmetric_difference(set_9))
print(set_9^set_99)

#10.Check if a set is empty.
sett= set()
print(sett)
print(bool(sett))
print(len(sett)==0)

#*************************************************************
#********************** dictionary ***************************

#1.Write a Python program to count the frequency of characters in a string using a dictionary.
freq_char={}
def count_freq_char(stri):
    for i in stri:
        if i in freq_char:
            freq_char[i]+=1
        else:
            freq_char[i]=1
given_str="chintapakadamdam"
count_freq_char(given_str)
print(freq_char)

#2.Merge two dictionaries and handle duplicate keys.
dic_1={"nithin":96,"venkat":99,"usha":100}
dic_2={"gandhi":76,"hitler":93,"venkat":95}
merge_dic=dic_1|dic_2
print(merge_dic)

#3. Retrieve a value from a dictionary without causing a KeyError if the key doesn't exist.
dict_1={"nithin":96,"venkat":99,"usha":100}
res=dict_1.get('nithin')
print(res) #it print 96
print(dict_1["nithin"]) #it print 96
#print(dict_1.get("nithi")) it raise error
print(dict_1["nithi"]) #it none

#4. Write a Python program to create a dictionary from two lists of equal length.
li1=[1,3,5,7]
li2=[2,4,6,8]
dic=dict()
dict_={}
for i in range(len(li2)):
    dic.update({li1[i]:li2[i]})
    dict_.setdefault(li1[i],li2[i])
print(dic)
print(dict_)

#5. Update a dictionary with new key-value pairs.

dic_up={}
dic_up.update({"nithin":95})
print(dic_up)

#6. Find the key with the maximum value in the dictionary {'a': 10, 'b': 20, 'c': 5}.
dc={'a': 10, 'b': 20, 'c': 5}
print(max(dc))

#7. Check if a given key exists in a dictionary.
key=input()
dc={'a': 10, 'b': 20, 'c': 5}
key_g=dc.get(key)
print(key_g==None)
if key_g!= None:
    print("given key exists in a dictionary")
else:
    print("given key not exists in a dictionary")

#8.Delete a key-value pair from a dictionary and return its value.
di_1={"nithin":96,"venkat":99,"usha":100}
del_k=di_1.pop("nithin")
print(del_k)
print(di_1)

#9. Sort a dictionary by its keys or values.
di_1={"nithin":96,"venkat":99,"usha":100}
sort_di=sorted(di_1.items(),key=lambda x:x[1])
print(dict(sort_di))
#10. Write a Python program to reverse the key-value pairs in a dictionary.
di={"a":1,"b":2,"c":3}
print(di)
rev_di={}
for i in di.items():
    rev_di.update({i[1]:i[0]})
print(rev_di)
rev_di2 = {value: key for key, value in di.items()}
print(rev_di2)

#*************************************************************
#********************** tuple ***************************
#1.Create a tuple containing numbers from 1 to 10 and access the 5th element.
tup=((1,2,3,4,5,6,7,8,9,10))
print(type(tup))
print(tup[4])

#1. Write a Python program to check if an element exists in a tuple.

tup_f=("mahesh","ramcharan","Kajal",123,156,True)
print(type(tup_f))
if "mahesh" in tup_f:
    print("element exist")
else:
    print("element not exist")
print("Element exists" if "mahesh" in tup_f else "Element does not exist")

#3.Convert a list [1, 2, 3, 4, 5] into a tuple.
list_tup=tuple([1, 2, 3, 4, 5])
print(list_tup)
print(type(list_tup))

#4.Find the length of the tuple (10, 20, 30, 40, 50).
l_tup=(10, 20, 30, 40, 50)
print(len(l_tup))

#5.Write a Python program to count the occurrences of the element 2 in the tuple (1, 2, 3, 2, 4, 2).
c_tup=(1, 2, 3, 2, 4, 2)
print(c_tup.count(2))

#6.Unpack the tuple (100, 200, 300) into three variables and print them.
a,b,c=(100, 200, 300)
print(a,b,c)
#7.Write a Python program to concatenate two tuples (1, 2, 3) and (4, 5, 6).
tup1=(1,2,3)
tup2=(4,5,6)
print(tup1+tup2)

#8.Convert the string "Python" into a tuple of characters.
st="Python"
st_tup=("Python",)
print(type(st_tup))
#9. Write a Python program to find the index of the first occurrence of 5 in the tuple (1, 3, 5, 7, 5, 9).
tup = (1, 3, 5, 7, 5, 9)
index = tup.index(5)
print("The index of the first occurrence of 5 is:", index)
second_index = tup.index(5, index + 1)
print("The index of the second occurrence of 5 is:", second_index)

#10.Explain why tuples are immutable and how this property can be useful in programming.
#Immutability means that once a tuple is created, its elements cannot be changed, added, or removed.
#Tuples in Python are designed to be immutable to ensure that their contents remain consistent throughout their lifetime. This immutability:
#Helps maintain data integrity by preventing accidental modification.
#Improves performance since immutable objects are often optimized internally by Python.
#Unlike lists, tuples are used when you want to ensure that the data does not change