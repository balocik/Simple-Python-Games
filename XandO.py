#---------------------------
#      08/10/2017
# created by Wojciech Kuczer 
#---------------------------

start = 1
while start == 1:
    # global variables
    X = "X"
    O = "O"
    EMPTY = " "
    TIE = "TIE"
    NUM_OF_SQUARES = 9

    #defining few functions
    def display_instruction():
        print("""
        Welcome in the biggest intelectual challange of all times
                                X an O
        It's a real war between human and computer. I'm computer and
        of course I'm better than You little human. If you think You are
        smarter than my processor power ceativity than proove it and win
        
        You will tell me Your moves by entering number of the square You
        would like to use to place your X or O
        
                        1 | 2 | 3
                        ---------
                        4 | 5 | 6
                        ---------
                        7 | 8 | 9
                        
        Get ready poor little human.\n
        """)

    def ask_yes_no(question):
        """Ask user question which only have option YES or NO"""
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response

    def ask_number(question, low, high):
        """Ask to enter number of square"""
        response = None
        while response not in range(low, high):
            response = int(input(question))-1
        return response

    def pieces():
        """Define who makes first move"""
        go_first = ask_yes_no("Would You like to make first move? (Y/N): ")
        if go_first == "y":
            print("\nSo You choose to go first. You need that You know it.")
            human = X
            computer = O
        else:
            print("\nYour currage will kill You.HAHAHA. I will make first move.")
            computer = X
            human = O
        return computer, human

    def new_board():
        """create new gameboard"""
        board = []
        for square in range(1,(NUM_OF_SQUARES+1)):
            board.append(EMPTY)
        return board

    def display_board(board):
        """Display board"""

        print("\n\t", board[0], "|", board[1], "|", board[2])
        print("\t", "---------")
        print("\t", board[3], "|", board[4], "|", board[5])
        print("\t", "---------")
        print("\t", board[6], "|", board[7], "|", board[8], "\n")

    def legal_moves(board):
        """List of legal moves"""
        moves = []
        for square in range(NUM_OF_SQUARES):
            if board[square] == EMPTY:
                moves.append(square)
        return moves

    def winner(board):
        """Find out who's the winner"""
        WAYS_TO_WIN = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 6))

        for row in WAYS_TO_WIN:
            if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
                winner = board[row[0]]
                return winner

        if EMPTY not in board:
            return TIE

        return None

    def human_move(board, human):
        """reads human move"""
        legal = legal_moves(board)
        move = None
        while move not in legal:
            move = ask_number("Your turn pick a square? (1-9): ", 0, NUM_OF_SQUARES)
            if move not in legal:
                print("this field is already taken You silly human. Try again:\n")
        print("Well done...")
        return move

    def computer_move(board, computer, human):
        """reads computer move"""
        #make board copy as function gonna change the list
        board = board[:]
        BEST_MOVES = (4,0,2,6,8,1,3,5,7)

        print("I choose square", end=" ")

        #if there's a chance computer can win choos the square
        for move in legal_moves(board):
            board[move] = computer
            if winner(board) == computer:
                print(move +1)
                return move
            #this move has been checked revers it
            board[move] = EMPTY

        #if human can win block his move
        for move in legal_moves(board):
            board[move] = human
            if winner(board) == human:
                print(move + 1)
                return move
            #this move has been checked revers it
            board[move] = EMPTY

        #if noone can win in the next move choose best possible move
        for move in BEST_MOVES:
            if move in legal_moves(board):
                print(move + 1)
                return move


    def next_turn(turn):
        """change turns"""
        if turn == X:
            return O
        else:
            return X

    def congratulations(the_winner, computer, human):
        if the_winner != TIE:
            if the_winner == computer:
                the_winner = "Computer"
                print(the_winner, "is the WINNER!\n")
                print("Just like I thought, once again I win and proof that You human can not beat me")
            else:
                the_winner = "Human"
                print(the_winner, "is the WINNER!\n")
                print("No No No.I can't be possible.You won this time human\n" \
                      "But next time You will defenetly loose.")
        else:
            print("TIE!\n")

        # if the_winner == computer:
        #     print("Just like I thought, once again I win and proof that You human can not beat me")
        # elif the_winner == human:
        #     print("No No No.I can't be possible.You won this time human\n" \
        #           "But next time You will defenetly loose.")
        if the_winner == TIE:
            print("You have been extremly lucky and somehow You achived TIE in this game.Next time I win")


    def main():
        display_instruction()
        computer, human = pieces()
        turn = X
        board = new_board()
        display_board(board)

        while not winner(board):
            if turn == human:
                move = human_move(board, human)
                board[move] = human
            else:
                move = computer_move(board, computer, human)
                board[move] = computer
            display_board(board)
            turn = next_turn(turn)

        the_winner = winner(board)
        congratulations(the_winner, computer, human)

    #start game
    main()
    start = int(input("\nTo play again enter- 1 , to Quit enter - 2"))

print("\nthanks for playing")






















