#---------------------------
#      06/10/2017
# created by Wojciech Kuczer 
#---------------------------

#final value
start = 1

while start == 1:
    HANGMAN = (
        """
         ------
         |    |
         |
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   -+-
         | 
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |    |
         |   | 
         |   | 
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |    |
         |   | |
         |   | |
         |  
        ----------
        """)

    MAX_WRONG = len(HANGMAN) - 1

    word = input("Enter word to guess: ")
    print("\n" * 100)
    word = word.upper()

    so_far = '*' * len(word)
    wrong = 0
    used = []

    print("Welcome to HANGMAN game. GOOD LOOK!!!")

    while wrong < MAX_WRONG and so_far != word:
        print(HANGMAN[wrong])
        print("You have used following letters:\n", used)
        print("So far mistery word looks like this:\n", so_far)

        guess = input("\n\nEnter letter that You think is in mistery word: ")
        guess = guess.upper()

        while guess in used:
            print("You have used that letter previously", guess)
            guess = input("\n\nEnter letter that You think is in mistery word: ")
            guess = guess.upper()

        used.append(guess)

        if guess in word:
            print("\nYES!", guess, " is in mistery word")

            #create new version of valiue so_far with guessed letter
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new
        else:
            print("Sorry but ", guess, " is not in mistery word")
            wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYour little guy has just been hanged")
    else:
        print("\nYou have WON")

    print("\nMistery word was - ", word)

    start = int(input("To play again enter - 1, to Quit enter - 2"))
    print("\nThanks for playing")













