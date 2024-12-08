from http.cookiejar import join_header_words
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

#/************************NUMBERS***************************
#************************************************************


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
    else:
        print("given number is prime")

#2. Find the greatest common divisor (GCD) of two numbers.
