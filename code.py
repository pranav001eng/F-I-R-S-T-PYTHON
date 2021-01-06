import random

print("Number guessing game")

number = random.randint(1, 9)

chances = 0

print("Guess a number (between 1 and 9):")

while chances < 5:

      GuessNumber = int(input("Enter your guess:- "))

      if GuessNumber == number:
         print("Congratulation YOU WON!!!")
         break

      elif GuessNumber < number:
         print("Your guess was too low: Guess a number higher than", GuessNumber)

      else:
         print("Your guess was too high: Guess a number lower than",   GuessNumber)
         chances += 1

      if not chances < 5:        
         print("YOU LOSE!!! The number is", number)