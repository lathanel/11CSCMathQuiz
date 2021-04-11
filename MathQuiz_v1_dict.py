#in this version a dictionary is created with questions and answers(as strings)
#there is no mathematical calculations involved in this exercise.
questions = {'2*6 ':  '12','2*5 ':  '10','2*8 ':  '16'}

#loop dictionary to get the user answer and values from dictionary
#comparing both user answer and dictionary values.

for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
        print("Correct!")
   
    else:
        print("You're Wrong!")

