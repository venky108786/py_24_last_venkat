# Exercise 1: Print first 10 natural numbers using while loop
import time
from random import random
from symbol import continue_stmt

for i in range(1,11):
    print(i)
print("*************************************************************")
# Exercise 2: Print the following pattern
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print("*********************************************************************")

# Exercise 3: Calculate sum of all numbers from 1 to a given number
given_number=int(input("enter number:  "))
summ=0
for i in range(1,given_number+1):
    summ+=i
print(summ)
print("*********************************************************************")

# Exercise 4: Print the following pattern
for i in range(10):
    for j in range(i):
        print(' ', end=' ')
    for j in range(10-i):
        print(j, end=' ')
    print()
print("*************************************************")
#Exercise 5: Write a program to reverse a given string using loops.
 #           Input: "hello" Output: "olleh"

inp="hello"
for i in reversed(inp):
    print(i,end="")
print("\n")
print("*************************************************")
#Exercise 6: Fibonacci Series
inp_fibanacci=int(input("enter fibanacci series:  "))
n,m=0,1
for i in range(inp_fibanacci):
    print(n,end=' ')
    n,m=m,n+m
print("\n")
print("*************************************************")
'''
Problem: Find All Unique Triplets That Sum to Zero
Write a Python program to find all unique triplets in a list of integers that sum to zero.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Requirements:
You must use loops to find the triplets.
The solution must avoid duplicates, meaning the same triplet cannot appear more than once in the output.
'''
li = [-1, 0, 1, 2, -1, -4]
sum_li = set()
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        for k in range(j + 1, len(li)):
            if li[i] + li[j] + li[k] == 0:
                sum_li.add(tuple(sorted((li[i], li[j], li[k]))))

print(sum_li)
print("*******************************************")
#Calculate the factorial of a given number using a while loop.
given_factorial=int(input("enter factorial: "))
fac=given_factorial
facto=1
while 1<fac:
    facto*=fac
    fac -= 1
print(facto)
print("\n")
print("********************//grocery//***********************")
dic={}
inp=input("enter item and qty: ").split(",")
dic.setdefault(inp[0],int(inp[1]))
#add=input("if you add item type (y/n): ")
while True:
    add = input("if you add item type (y/n): ")
    if add.lower()=="y":
        add_2=input("enter item,qty: ").split(",")
        dic.setdefault(add_2[0], int(add_2[1]))
    elif add=="n":
        break
summ=0
for item,qty in dic.items():
    print(f'{item:} {qty}')
    summ+=qty
print(summ)


print("************ \"cricket match\"*************")
'''
concept:- two teams SRH and CSK filp a coin who toss win that team play batting first 
after that bowling team play batting compare both team score which team get more score 
that team win if draw the match play again
'''
def flip_coin(coin):
    x = int(random()*2)
    if coin.lower() in ["tail","head"]:
        if x==0:
            toss="tail"
            print(toss)
        else:
            toss="head"
            print(toss)

        if coin.lower()==toss:
            return "you won toss now take batting"
        else:
            return "you loss toss now take bowling"
    else:
        return "please select valid toss"

while True:
    print("SRH vs CSK")
    select_your_team=input("enter your team like above mentioned name: ")
    if select_your_team.upper() in ["SRH","CSK"]:
        print("Loading...")
        time.sleep(2)
        print("now toss time select head or tail")
        coin=input()
        result=flip_coin(coin)
        print(result)
    else:
        print("please select enter valid team")
