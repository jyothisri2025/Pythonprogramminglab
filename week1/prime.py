n=int(input("enter the number:"))
x=0
for i in range(2 , n):
    if(n%i == 0):
        print("not a prime")
        x=2
        break;
if( x==0 ):
    print("prime")
