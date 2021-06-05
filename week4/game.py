import random
import math

lowest = int(input("Enter a number 1 here: "))
highest = int(input("Enter a number 9 here: "))

x = random.randint(lowest, highest)
print("\n\tYou've only have", 
       round(math.log(highest - lowest + 1, 2)),
      "chances to guess the number!\n")

count = 0

while count < math.log(highest - lowest + 1, 2):
    count += 1
 
    guess = int(input("Guess a number: "))
 
    if x == guess:
        print("Great job, you guessed it in the",
              count, "try!")
        break
    elif x > guess:
        print("The number you guessed is too low!")
    elif x < guess:
        print("The number you guessed is too high!")
 
if count >= math.log(highest - lowest + 1, 2):
    print("\nThe number is %d" % x)
    print("\t Sorry you did not get it correct! Better Luck Next time!")