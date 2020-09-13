"""Q3
Write a Python function that takes a sequence of integer values and determines if there is a distinct pair of
numbers in the sequence whose product is odd."""


#function to form all possible pairs from the sequence of integers and check if product of numbers in any of the pair is odd.
def checkoddproductpair(n,lst):
    count=0
    
    #Using 2 for loops we can check product of all possible pairs
    for i in range(0,n):
        for j in range(i+1,n):
            
            product=(lst[i]*lst[j])
            
            #count no. of product which are odd
            if (product%2==1):
                count+=1

    if(count==0):
        return "No pair there is no such pair in the above sequence of integers whose product is odd."
    else:
        return "Yes there is a pair in the above sequence of integers whose product is odd."
    

n=int(input("Enter number of elements in the integer sequence: "))
lst=[]
for i in range(n):
    lst.append(int(input("Enter element: ")))
    
print(checkoddproductpair(n,lst))