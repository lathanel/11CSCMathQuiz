import random


def instructions():
    inst=input("do you need instructions enter y or n : ")
    if inst=="y":
        print("you can choose any number of rounds")
        print("choosing small number is easy")
    else:
        print("Welcome to Math Quiz")
    
instructions() 

def get_range():
    num=int(input("Please enter number of questions you would like to play:"))
    return num
num=get_range()
#Sets score to 0
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
print("You got "+str(score)+" right!")
##for k,v in questions.items():
##    print(k,v)
 
 
