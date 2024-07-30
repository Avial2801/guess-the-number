import random
count = 8
red = random.randint(0,9)
no_repeat = set()
while count >0:
    n = int (input(("enter the number between 0 to 9  ")))
    if n in no_repeat:
            print("This number has already been entered. Try again.")
            continue    
    no_repeat.add(n)
    if red !=n:
        print("green")
    elif red==n:
        print("red")
        print ("you lost")
        break
    count = count - 1
    print ( " you have only this much chances ",count)
    if count == 1 :
        print("this is last chance")

print ("game over")
    

