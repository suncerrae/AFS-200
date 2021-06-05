import random
import math

exit = False
while exit is not True:
    lowest = 1
    highest =9

    x = random.randint(lowest, highest)
    print("\n\tYou've only have", 
        round(math.log(highest - lowest + 1, 2)),
        "chances to guess the number!\n")

    count = 0

    while count < math.log(highest - lowest , 2):
        count += 1
        guess = (input("Guess a number: "))
        if len (guess)<2:
            if x == int (guess): 
                print("Great job, you guessed it in the",
                    count, "try!")
                break
            elif x > int (guess): 
                print("The number you guessed is too low!")
            elif x < int (guess): 
                print("The number you guessed is too high!")
            if count == math.log(highest - lowest , 2) and x is not int (guess):
                print("\nThe number is %d" % x)
                print("\t Sorry you did not get it correct! Better Luck Next time!")
        else:
            exit=True 
            break
    
       
print("Bye Bye")