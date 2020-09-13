#Question2
"""
Q2. What parameter values should be sent to the range constructor to produce a range with values:
(a) 60,70,80
(b) 4,2,0,-2,-4
"""

#Solution:
"""
(a) 60,90,10 should be sent to the range constructor, since we know *range constructor* takes (start, stop, step) as input, where *stop* is not included in the range. So the range will start at 60, then increase by 10 as step=10 so next value will be 70, then 80, then next value should be 90 but as stop=90 so 90 will not be included in the range.
"""
#Program to verify:
print(list(range(60,90,10)))

    

"""
(b) 4,-6,-2 should be sent to the range constructor. So the range will start at 4, then decrease by -2 as step=-2 so next value will be 2, then 0, then -2, then -4 and then next value should be -6 but as stop=-6 so -6 will not be included in the range.
"""
#Program to verify:
print(list(range(4,-6,-2)))


