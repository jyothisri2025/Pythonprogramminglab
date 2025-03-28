x=input("Enter ")[0]
if x.islower():
      print("{} is in lower case".format(x[0]))
elif x.isupper():
      print("{} is in upper case".format(x[0]))
elif x.isdigit():
      print("{} is a digit".format(x[0]))
else :
      print("It is a special character")
