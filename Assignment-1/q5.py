"""Q5
Write a Python program that takes as input three integers, “a”, “b” and “c”, from the console and
determines if they can be used in the following arithmetic formulas: (i) “a+b=c”, (ii) “a=b-c”, (iii) “a*b=c”."""


a= int(input("Enter a: "))
b= int(input("Enter b: "))
c= int(input("Enter c: "))

if (a+b==c):
    print("YES, they can be used in a+b=c")
else:
    print("NO, they can't be used in a+b=c")

    
if (a==b-c):
    print("YES, they can be used in a=b-c")
else:
    print("NO, they can't be used in a=b-c")
    

if (a*b==c):
    print("YES, they can be used in a*b=c")
else:
    print("NO, they can't be used in a*b=c")