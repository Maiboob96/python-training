Syntax od range():
    range(stop)
    range(start, stop, [, step])
    
1)  
print (list (range(10)))

print (list (range(20)))

print (list (range(15)))


2)
from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
         print(i, end=' ')
    print()


3)    
#printing first 5
#whole number

for i in range(5):
    print(i, end=" ")
print()

# printing first 15
#whole number

for i in range(15):
    print(i, end=" ")
    
4)
# Python program to
# print all number
# divisible by 3 and 5

# using range to print number
# divisible by 3
for i in range(0, 30, 3):
    print(i, end=" ")
print()

-----------------


# incremented by 2
for i in range(2, 20, 2):
    print(i, end=" ")
print()

# incremented by 4
for i in range(0, 25, 4):
    print(i, end=" ")
print()

# incremented by 3
for i in range(15, 30, 3):
    print(i, end=" ")
--------------------------

Concatenation of two range() functions

# Python program to concatenate
# the result of two range functions
from itertools import chain

# Using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))

for i in res:
    print(i, end=" ")
    
 
