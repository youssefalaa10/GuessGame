# This is a guess the number game.
import random

guessesTry = 0

name = input("Hello! What is your name? : "  )  #player name
number = random.randint(1, 20)

print('Ok, ' + name + ', I\'m thinking of a number between 1 and 20.')

while guessesTry < 6:    #num of tries

    print('Take a guess.') 
    guess = input()
    guess = int(guess)

    guessesTry = guessesTry + 1

    if guess < number:
        print('Your guess is too low.') 

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
      break

if guess == number:
 guessesTry = str(guessesTry)
 print('Good guess, ' + name + '! You guessed my number in ' + guessesTry + ' guesses!')

if guess != number:
 number = str(number)
 print('You loss. The number I was thinking of was ' + number)