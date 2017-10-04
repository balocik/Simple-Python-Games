#---------------------------
#      04/10/2017
# created by Wojciech Kuczer 
#---------------------------

# In this game computer mix letters in word which is chosen from list.
# user has to find out what is the original word

import random

start = 1
while start != 2:

    WORDS = ("python", "dady", "mouse", "computer", "keyboard", "kajak")
    word = random.choice(WORDS)
    correct = word

    # computer mixing word
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position +1):]

    #Instructions for player
    print("""
                        Welcome in my game!
                        
            Order characters in given 'jumble' word to make real word.
            If You think it's to hard and want to give up enter number "9"
    """)

    print("\nWhat's that word: ", jumble)
    #User enters his/her guess
    guess = input("Enter Your guess: ")
    while guess != correct and guess != "9":
        print("\nSorry. Please try again")
        guess = input("Enter Your guess: ")

    if guess == correct:
        print("\nYou WON. Your answer is correct")

    start = int(input("\nTo play again press - 1, to Quit press - 2"))

print("\nThanks for playing")
