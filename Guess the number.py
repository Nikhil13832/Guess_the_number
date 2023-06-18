import random
num_1 = random.randint(0, 9)
a = None
while a != num_1:
    a = input("guess a number between 0 to 9: ")
    a = int(a)
    
    if a == num_1:
      print("You guessed it right, it is " + num_1)
      break
    else:
     print("try again")
