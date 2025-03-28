n=int(input("Enter the series length"))
a=0
b=1
while n>0 :
       print(a,end=" ")
       c=a+b
       a=b
       b=c
       n=n-1