-1) # prints python programs 3 Times
count = 0
while (count < 3):
    count = count+1
    print("python programs")
    
 2)
a = 33
b = 200
if b > a:
  print("b is greater than a")

3)
a = 96
b = 96
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
---------------
->Else
 The else keyword catches anything which isn't caught by the preceding conditions.
    
In this example a is greater than b, so the first condition is not true, also the elif condition is not true, 
so we go to the else condition and print to screen that "a is greater than b".

4)
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

5)
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

-----------------------------

Nested If
You can have if statements inside if statements, this is called nested if statements.

6)

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
---------------------------------------
7)
i = 1
while i < 6:
  print(i)
  i += 1

    8)
-> Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

8) 
# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")


---------------------------------------------


if statement
---------------

num = 5
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")


if...else
------------------

# Program checks if the number is positive or negative
# And displays an appropriate message

num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")



if...elif...else Statement
-------------------------------

'''In this program, 
we check if the number is positive or
negative or zero and 
display an appropriate message'''

num = -5.5

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")




num = 10.5

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


Nested if statements
-------------------------

'''In this program, we input a number check if the number is positive or
negative or zero and display an appropriate message
This time we use nested if statement'''

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")




    
