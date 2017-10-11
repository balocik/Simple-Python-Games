#---------------------------
#      11/10/2017
# created by Wojciech Kuczer 
#---------------------------

import sys

def open_file(file_name, mode):
    """Opening file"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Cant open file ", file_name, "Application will terminate.\n", e)
        input("\n\nTo quit press ENTER")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Read line by line out of provided txt file"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return next part of quiz"""
    category = next_line(the_file)
    question = next_line(the_file)
    
    #create list of answers
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, correct, explanation

def welcome(title):
    """Greet user"""
    print("\t\tWelcome in knowledge quiz")
    print("\t\t", title, "\n")

def main():
    quiz_file = open_file("quiz.txt", "r")
    title = next_line(quiz_file)
    welcome(title)
    score = 0

    #read firs block of the quiz
    category, question, answers, correct, explanation = next_block(quiz_file)
    while category:
        #ask question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i +1, "-", answers[i])

        #get user's answer
        answer = input("Enter Your answer (1-4)\n\n\n")

        if answer == correct:
            print("\nWell done.Your answer is correct. You got a point", end=" ")
            score += 1
        else:
            print("\nSorry wrong answer.", end=" ")
        print(explanation)
        print("Points: ", score, "\n\n")

        #load another bloc of quiz
        category, question, answers, correct, explanation = next_block(quiz_file)

    quiz_file.close()

    print("\nthat was last question!")
    print("\nYour total score is ", score)

main()
print("\nThanks for playing")
input("\nTo Exit the game press enter")





















    