import random,math,time
from pynput import keyboard


def retries(m,n):
    return round(math.log2(abs(m-n)))


#Input name and range
playerName=input("What is your name?:")
print(f'\n\tWELCOME TO GUESS THE NUMBER ', playerName.upper(),'!!')
print('Enter the range you want to play in(start and end)....')
rangeStart=int(input("Range start:"))
rangeEnd= int(input("Range end:"))


def game(rangeStart,rangeEnd):
    chances=retries(rangeStart,rangeEnd) 
    print(f'You will get a total of {chances} chances......')
    time.sleep(2)
    gameNum=random.randint(rangeStart,rangeEnd)

    for i in range(chances):
        print(f'\n\t\tGuess Number {i+1}')
        print('\t\tEnter your guess:' ,end="")
        guess=int(input())

        if(guess>gameNum):
            print(f'\t\tToo high, try again')

        elif(guess<gameNum):
            print('\t\tToo low,try again')

        else:
            break
    time.sleep(1)
    if(guess==gameNum):
     print(f'\n\n<----------Congrats!!,you guessed it in {i+1} tries------------->')
    else:
     print(f'\n\n<----------Too Bad!!The correct answer was{gameNum},Try again---------->')
     


game(rangeStart,rangeEnd)

time.sleep(1)
playAgain=input('\nEnter Y,Yes, or press the Enter button to play again......') 
if(playAgain.lower()=="y" or playAgain.lower()=="yes"):
    time.sleep(1)
    print('\n')
    game(rangeStart,rangeEnd)


