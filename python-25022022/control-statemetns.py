-> # prints python programs 3 Times
count = 0
while (count < 3):
    count = count+1
    print("python programs")
    
 
a = 33
b = 200
if b > a:
  print("b is greater than a")


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

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

-----------------------------

Nested If
You can have if statements inside if statements, this is called nested if statements.


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

    
    
