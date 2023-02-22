import time
import random

b=random.randrange(1,20)
red=0
while red < 105 :
    guess = int(input("input any digit : "))
    red +=1
    if guess< b : 
        print("too low")
        
    if guess > b : 
        print("too high") 
        
    if guess == b :
        break
if guess == b :
    print("you guessed the number in " + str(red) + " tries")
else :
    print("you didn't guess the number, the number was " +str(b))    