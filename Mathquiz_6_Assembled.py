import random
def yourname():
    fname= input("First Name :")
    lname= input("Last Name :")
    fullname =fname+" "+lname
    return fullname
             

def instructions():
    inst=input("do you need instructions enter y or n : ")
    if inst=="y":
        print("you can choose any number of rounds")
        print("choosing small number is easy")
    else:
        print("Welcome to Math Quiz")
fullname = yourname()   
instructions() 

def get_range():
    num=int(input("Please enter number of questions you would like to play:"))
    return num
num=get_range()
#Sets score to 0
mname = " my name"
score=0
#initialises dictionary
questions = {}

#Randomly generates maths questions with number between 0 and 10
#Operator is randomly picked out of (+, -, *)
for i in range(num):
    int_a = random.randint(0,10)
    int_b = random.randint(0,10)
    operators = ['+','-','*']
    operator_value = random.choice(operators)
    question = str(int_a)+" "+operator_value+" "+str(int_b)
    answer = str(eval(question))
    question+=": "
    
    #adds the question to questions dictionary
    if not question in questions.keys():
      questions.update({question:answer})
    else:
      continue
    

#Iterates through the questions in the dictionary and response respectively
for q in questions.keys():
    user_answer=input(q)
    if questions.get(q)==user_answer:
        print("Correct!")
        score+=1
    else:
        print("You're Wrong!")
#Outputs the users score
print("Game stats")
print("")
print("----------------")
games=len(questions)
percent=(score/games)*100
txt = "{fullname:s} you have played {games:d} games and Your success rate is {percent:.2f} "
print(txt.format(fullname=fullname,games=games,percent = percent))


 
 
