from random import random, randrange, randint

def game(name):
    number = randint(1, 20)
    guesses = 1
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    while True:
        print('Take a guess.')
        g = int(input())
        if g == number:
            print(f'Good job, {name}! You guessed my number in {guesses} guesses!')
            break
        else:
            print('Your guess is too low.')
            guesses+=1
    
    
print('Hello! What is your name?')
name = input()
game(name)