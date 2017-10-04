#---------------------------
#      02/10/2017
# created by Wojciech Kuczer 
#---------------------------

# Game where user has to guess number

import random

start = 1

while start == 1:
    #generates random number 1-100
    number = random.randint(1,100)
    guess_counter = 10
    print("Please guess my number in range 1 to 100")
    print("You have 10 tries to do it")

    #loop for user to guess number in 10 tries
    while guess_counter > 0:
        #ask user for his/her guess

        user_guess = input("\nEnter number: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("I'm affrid {} is not a number".format(user_guess))
            print("\nEnter number between 1 and 100")
            continue
        else:
            if user_guess == number:
                print("\nCongratulation You won")
                break
            elif user_guess < number:
                guess_counter -= 1
                print("\nGuess higher next time")
                print("\nYou have " + str(guess_counter) + " guesses left")

            else:
                guess_counter -= 1
                print("\nGuess lower next time")
                print("\nYou have " + str(guess_counter) + " guesses left")


    #ask user wheather he/she wants to play again
    if guess_counter <= 0:
        print("\nYou lost. Better luck next time")
        start = int(input("\nTo play again enter 1 to Quit enter 2: "))
    else:
        start = int(input("\nTo play again enter 1 to Quit enter 2: "))
print("\nThanks for Playing with me.See You soon I hope.")