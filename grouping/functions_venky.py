from random import random
while True:
    def guessing_number_game(num):
        if 0<num<10:
            rn=int(random()*10)
            if rn==num:
                return "you got price"
            else:
                return "better luck next time"
        else:
            return "please enter with range"


    given_num=int(input('''please enter your guessing
number between 1 to 10:  '''))

    print(guessing_number_game(given_num))
