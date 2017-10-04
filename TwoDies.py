#---------------------------
#      01/10/2017
# created by Wojciech Kuczer 
#---------------------------

import random


numer = 1
while numer == 1:
    die1 = random.randint(1, 6)
    die2 = random.randrange(6) + 1
    print("\nDie 1: " + str(die1))
    print("\nDie 2: " + str(die2))
    print()
    print("Result is: " + str(die1 + die2))
    numer = int(input("\nPlay again - 1. \nFinish game - 2\n\n"))
print("\nThanks for playing")