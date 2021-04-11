# this program will ask user if they want instructions to play the quiz.
def instructions():
        print("you can choose any number of rounds")
        print("for each correct answer, you get a score of 1")
        print("you will get the summary of your score at the end of the quiz.")
        print("score statistics like percentage will also be displayed at the end of the game.")
def instructions_choice():
    inst=input("do you need instructions? enter y or n : ").lower()
    if inst in [ "y", "yes" ]:
        instructions()
         
    elif inst in ["no","n","N","NO" ]:
        print("Welcome to Math Quiz")
    elif inst in ["may be",""]:
        inst=input("You need to enter something.do you need instructions? enter y or n : ").lower()
        if inst in ["y","yes"]:
            instructions()
        else:
            print("Welcome to Math Quiz")
        
instructions_choice()
