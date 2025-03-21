// compound intrest
p=int(input("enter principle "))
r=int(input("enter the percent rate:"))
n=int(input("per year:"))
a=p*(1+r)/100**(n)
ci=a-p
print(round(ci,2))

