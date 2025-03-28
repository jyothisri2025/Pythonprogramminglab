import random
n=random.randint(1 , 100)
print(n)
count = 8
while count > 0:
        x=int(input("enter a number:"))
        if x == n:
                print("Successful")
                break
        elif x > n :
                print("too high")
        else :
                print("too low")
        count = count-1
print("YOUR FAILED!TRY AGAIN DUDE") 
