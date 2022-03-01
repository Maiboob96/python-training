List methods in Python
___________________________

Types of List Method
----------------------------
Python List index()
Python List append()
Python List extend()
Python List insert()
Python List remove()
Python List count()
Python List pop()
Python List reverse()
Python List sort()
Python List copy()
Python List clear()


(1) List index() 
___________________________________________________________
    
index(): Returns the index of first occurrence. Start and End index are not necessary parameters.
-> The index() method returns the index of the specified element in the list.
Syntax:
List.index(element[,start[,end]])


Programs:
_________
1)
language = ['c', 'java', 'python', 'groovy']

# get the index of 'python'
index = language.index('python')


print(index)

2)
List = [1, 2, 6, 5, 2, 8, 2, 3, 2, 9]
print(List.index(8))

3) Index of the Element not Present in the List
# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# index of 'p' is vowels
index = vowels.index('p')

print('The index of p:', index)

Index of the Element Present in the List

# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# index of 'p' is vowels
index = vowels.index('o')

print('The index of o:', index)

4) index of element
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')

print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')


print('The index of i:', index)




(2) List append():
    _____________________________________________________________________________________________
    Used for appending and adding elements to List.It is used to add elements to the last position of List.
Syntax: 
    list.append (element)
    
append() Parameters
The method takes a single argument
    
    Programs:
    _________
    
1)
# Adds List Element as value of List.
List = ['python', 'java', 1996, 2022]
List.append("ansible")
print(List)

2)

# animals list
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox']

# appending wild_animals list to animals
animals.append(wild_animals)

print('Updated animals list: ', animals)

3) List extend():
  __________________________________________________________

extend(): Adds contents to List2 to the end of List1.
Syntax:
List1.extend(List2)

Programs:
---------
1)
List1 = [1, 2, 3]
List2 = [4, 8, 9, 5]

# Add List2 to List1
List1.extend(List2)
print(List1)

# Add List1 to List2 now
List2.extend(List1)
print(List2)

2)
# languages list
languages = ['French', 'English']

# another list of language
languages1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
languages.extend(languages1)


print('Languages List:', languages)

3)
a = [1, 2]
b = [3, 4]

a += b    # a = a + b

print('a =', a)

# Output: [1, 2, 3, 4]

4) List insert():
   ___________________________________________________
Inserts an elements at specified position.
Syntax:
 list.insert(<position, element)

Programs:
----------
1) inserting an element to the list
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# insert 11 at index 4
prime_numbers.insert(4, 11)


print('List:', prime_numbers)

2) inserting tuple to the list

mixed_list = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list
mixed_list.insert(1, number_tuple)


print('Updated List:', mixed_list)

3)
List = ['python', 'java', 2000, 2022]
# Insert at index 2 value 10087
List.insert(2,1996)
print(List)

5) List remove():
  ______________________________________
The remove() method removes the first matching element (which is passed as an argument) from the list.
Syntax:
    list.remove(element)
 remove() Parameters
The remove() method takes a single element as an argument and removes it from the list.
If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.

Programs:
----------------
1)
# animals list
animals = ['cat', 'dog', 'rabbit', 'elephant']

# 'rabbit' is removed
animals.remove('elephant')


# Updated animals List
print('Updated animals list: ', animals)

2)
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3)
print(List)

4)
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# Deleting 'fish' element
animals.remove('fish')


# Updated animals List
print('Updated animals list: ', animals)


output:
Traceback (most recent call last):
  File ".. .. ..", line 5, in <module>
    animal.remove('fish')
ValueError: list.remove(x): x not in list

5) count():
 _______________________________________________________________
Calculates total occurrence of given element of List.
Syntax:
List.count(element)
count():Calculates total occurrence of given element of List.
Syntax:
List.count(element)

Return value from count()
The count() method returns the number of times element appears in the list.

Programs:
------------
Example 1:
# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)


Example 2: Use of count
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)

Example 3:
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

6) List pop():
_____________________________________
The pop() method removes the item at the given index from the list and returns the removed item.
Syntax:
    list.pop(index)
    
pop() parameters
The pop() method takes a single argument (index).
The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
If the index passed to the method is not in range, it throws IndexError: pop index out of range exception.
    
Return Value from pop()
The pop() method returns the item present at the given index. This item is also removed from the list

Programs:
---------------
Example 1: Pop item at the given index from the list
 # programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)

print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)

7) List reverse():
 ______________________________________
The reverse() method reverses the elements of the list.

Syntax:
    list.reverse()
    
reverse() parameter
The reverse() method doesn't take any arguments.
Return Value from reverse()
The reverse() method doesn't return any value. It updates the existing list.

Programs:
-----------------
Ex 1)
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# List Reverse
systems.reverse()


# updated list
print('Updated List:', systems)

Ex 2:Accessing Elements in Reversed Order
# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)

    
8) List sort():
__________________________________________

The sort() method sorts the elements of a given list in a specific ascending or descending order.

Syntax:
    list.sort(key=..., reverse=...)
    
sort() Parameters
By default, sort() doesn't require any extra parameters. However, it has two optional parameters:

reverse - If True, the sorted list is reversed (or sorted in Descending order)
key - function that serves as a key for the sort comparison

sort() Return Value
The sort() method doesn't return any value. Rather, it changes the original list.

If you want a function to return the sorted list rather than change the original list, use sorted().

Programs:
Ex 1: sort a given list
    
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)

Ex 2: sor the list in Descending order
 # vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list (in Descending):', vowels)


Ex 3: sort the list using key
    
# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)
