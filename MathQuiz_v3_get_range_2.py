 

def get_range():     
    
        while True:
            try:
                num=int(input("Please enter a number between 1 and 10:"))
                if num >=1 and num <=10:
                    print("ok")
                    break 
                 
            except ValueError: 
                print("Invaild input. Please enter a whole number")
         

get_range() 
