#---------------------------
#      14/10/2017
# created by Wojciech Kuczer 
#---------------------------

class Player(object):
    """game player"""
    def __init__(self,name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Ask question with option of response YES or NO"""
    response = None
    while response not in ("Y", "N"):
        response = input(question).upper()
    return response

def ask_number(question, low, high):
    """Poproś o podanie liczby z określonego zakresu."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("You shouldn't use this modul directly.Import it please")
    input("\n\nPress Enter to Finish")
