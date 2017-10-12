#---------------------------
#      12/10/2017
# created by Wojciech Kuczer 
#---------------------------

class Pet(object):
    """virtual pet"""
    def __init__(self,name, hunger = 0, boredom =0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "very happy"
        elif 5 <= unhappines <= 10:
            m = "happy"
        elif 10 <= unhappines <=15:
            m = "sad"
        else:
            m = "angry"
        return m

    def talk(self):
        print("My name is {} and I'm {} now".format(self.name, self.mood))
        self.__pass_time()

    def eat(self, food = 4):
        print("Yum yum. Thank You")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        print("\nI'm {} now".format(self.mood))
        self.__pass_time()

    def play(self, fun = 4):
        print("Yuupee!!!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        print("\nI'm {} now".format(self.mood))
        self.__pass_time()


def main():
    crit_name = input("Enter Your pets name: ")
    crit = Pet(crit_name)

    choice = None
    while choice != "0":
        print(
            """
            You are a pet owner. What would you like to do with You pet:
            
            0 - Quit game
            1 - listen Your pet
            2 - feed Your pet
            3 - play with Your pet
            """
        )

        choice = input("Choose an option: ")

        if choice == "0":
            print("Good bye")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("Soory but Your selection is not correct")

main()
print("Thanks for playing")






















