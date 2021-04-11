def get_range():

    while True:
      try:
        num=int(input("Please enter a number you would like to play:"))
        return num
      except Exception as e:
        print(e)
num=get_range()
print(num)
