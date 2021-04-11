##''' this program gets user details such as name and age.
#defining the user_details function with one parameter
def user_details(name):
    greet = name
    print("hello", greet)

#The following code will accept even lower cases but will not accept numbers.    
name=""
while True:
    name = input("Please enter your name : ").lower()
    if name.isalpha():
        break
    print("Please enter characters A-Z only")
  

user_details(name)
print("process finished with calling function")
