from random import random
def guessing_number_game(numb):
    if numb.isnumeric():
        num=int(numb)
        if 0<num<10:
            rn=int(random()*10)
            if rn==num:
                return "you got price"
            else:
                return "better luck next time"
        else:
            return "please enter with range"
    else:
        return "only enter numbers"
while True:
    given_num=input('''please enter your guessing
number between 1 to 10:''')
    output_of=guessing_number_game(given_num)
    print(output_of)
    play_again = input("play again yes/no: ").lower()
    if play_again != 'yes':
        print("Thanks for playing")
        break


#//////////////02.12.20024 task-1 multiples//////
def multiples(mul):
    li=[]
    for i in range(1,11):
        li.append(f'{mul}*{i}={i*mul}')
    return li

x=input("enter multiple: ")
if x.isnumeric():
    result=multiples(int(x))
    print(*(result),sep="\n")
else:
    print("please endter correct data")


#/////////////////////task-2 arguments passing////////////////
def filling_rhymes(a,b,c):
    print(f'''ohny, Johny.
    Yes, {a}?
    Eating sugar?
    No, Papa. 
    {b} lies?
    No, Papa.
    Open your {c}.
    Ha-ha-ha!... ''')
a="papa"
b="telling"
c="mouth"
filling_rhymes(a,b,c)
#/////////////////////////////// above game/////////////////////
def filling_rhymes_game(a,b,c):
    print(f'''ohny, Johny.
    Yes, {a}?
    Eating sugar?
    No, Papa. 
    {b} lies?
    No, Papa.
    Open your {c}.
    Ha-ha-ha!... ''')
a=input("fill the rhyme_a: ")
b=input("fill the rhyme_b: ")
c=input("fill the rhyme_c: ")
filling_rhymes_game(a,b,c)



