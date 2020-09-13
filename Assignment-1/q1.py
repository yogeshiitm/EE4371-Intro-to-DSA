"""Q1
(a) Write a Python function that takes a positive integer n, and returns the sum of the squares of all
the positive integers smaller than n.

(b) Write a Python function that takes a positive integer n, and returns the sum of the squares of all
the odd positive integers smaller than n.
"""


#this function returns the sum of the squares of all the positive integers smaller than n.
def sumofsquares(n):
    sum=0
    for i in range(n):
        sum = sum + i*i
    return sum

#this function returns the sum of the squares of all the odd positive integers smaller than n.
def sumofoddsquares(n):
    sum=0
    """in this for loop, i will take the values 1,3,5,... so we will get sum of odd squares only"""
    for i in range(1,n,2):
        sum = sum + i*i
    return sum
    

n=int(input("Enter n: "))
print("Sum of squares of all the positive integers smaller than n =",sumofsquares(n))
print("Sum of squares of all the odd positive integers smaller than n =",sumofoddsquares(n))