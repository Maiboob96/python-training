                Python Dictionary Methods
  _________________________________________________________________________
  
Types of Python Dictionary Methods
---------------------------------------
Dictionary clear()
Dictionary copy()
Dictionary fromkeys()
Dictionary get()
Dictionary items()
Dictionary keys()
Dictionary pop item()
Dictionary setdefault()
Dictionary pop()
Dictionary values()
Dictionary update()



(1) Dictionary Clear():
  --------------------------------------------------
  The clear() method removes all items from the dictionary.
  
Syntax:
       dict.clear()
    
clear() Parameters
clear() method doesn't take any parameters.

Return Value from clear()
clear() method doesn't return any value (returns None).

Programs:
-----------

Exp 1:
  
d = {1: "one", 2: "two"}

d.clear()
print('d =', d)

Exp 2:
  
# Python code to demonstrate difference
# clear and {}.

text1 = {1: "python", 2: "java"}
text2 = text1

# Using clear makes both text1 and text2
# empty.
text1.clear()

print('After removing items using clear()')
print('text1 =', text1)
print('text2 =', text2)

text1 = {1: "one", 2: "two"}
text2 = text1

# This makes only text1 empty.
text1 = {}

print('After removing items by assigning {}')
print('text1 =', text1)

(2) Dictionary Copy():
----------------------------------------
Python Dictionary copy() method returns a shallow copy of the dictionary.

Syntax:
      dict.copy()
    
copy() Arguments
The copy() method doesn't take any arguments.

copy() Return Value
This method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.

Programs:
-----------
Exp 1:How copy works for dictionaries
  
original = {1:'one', 2:'two'}
new = original.copy()


print('Orignal: ', original)
print('New: ', new)

Exp 2:Using = Operator to Copy Dictionaries
  
original = {1:'one', 2:'two'}
new = original

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)

Exp 2:  Using copy() to Copy Dictionaries
  
original = {1:'one', 2:'two'}
new = original.copy()

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)

(3) Dictionary fromkeys()
-----------------------------------------------------


The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.
Syntax:
      dictionary.fromkeys(sequence[, value])
Programs:
  
Exp 1:

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print(vowels)

Exp 2:

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)

Exp 3:
  
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updating the value
value.append(2)
print(vowels)

Exp 4:

# to initialize dictionary with list
# using fromkeys()

# using fromkeys() to construct
new_dict = dict.fromkeys(range(4), [])

# printing result
print("New dictionary with empty lists as keys : " + str(new_dict))

(4) Dictionary get()
---------------------------------------------------------------------
The get() method returns the value for the specified key if the key is in the dictionary.

Syntax:
      dict.get(key[, value]) 
    
 
get() Parameters
get() method takes maximum of two parameters:

key - key to be searched in the dictionary
value (optional) - Value to be returned if the key is not found. The default value is None.


Return Value from get()
get() method returns:

the value for the specified key if key is in the dictionary.
None if the key is not found and value is not specified.
value if the key is not found and value is specified.

Programs:
Exp 1:
dic = {"A": 1, "B": 2}
print(dic.get("A"))
print(dic.get("C"))
print(dic.get("C", "Not Found ! "))

Exp 2:
person = {'name': 'Robert', 'age': 25}

print('Name: ', person.get('name'))

print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))

(5) Dictionary items():
 ----------------------------------------------------
The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.

Syntax:
      dictionary.items()

items() Parameters
The items() method doesn't take any parameters.

Return value from items()
The items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.

Programs:
---------------
Exp 1: Get all items of a dictionary with items()
# random languages dictionary
languages = { 'python': 2, 'java': 3, 'c': 4 }

print(languages.items())

Exp 2: How items() works when a dictionary is modified
  
# random languags dictionary
languages = { 'python': 2, 'java': 3, 'jenkins': 4 }

items = languages.items()

print('Original items:', items)

# delete an item from dictionary
del[languages['jenkins']]

print('Updated items:', items)  

(6) Dictionary keys():
---------------------------------------------
The keys() method returns a view object that displays a list of all the keys in the dictionary

Syntax:
       dict.keys()

keys() Parameters
keys() doesn't take any parameters.

Return Value from keys()
keys() returns a view object that displays a list of all the keys.

When the dictionary is changed, the view object also reflects these changes.

Programs:
--------------
Exp 1: How key() works

person = {'name': 'Robert', 'age': 25, 'salary': 5000.0}
print(person.keys())

empty_dict = {}
print(empty_dict.keys()
      
Exp 2: How keys() works when dictionary is updated
person = {'name': 'Robert', 'age': 25, }

print('Before dictionary is updated')
keys = person.keys()
print(keys)

# adding an element to the dictionary
person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)


Exp 3:
# Python program to demonstrate
# working of keys()

# initializing dictionary
test_dict = {"python": 7, "for": 1, "programs": 2}

# accessing 2nd element using naive method
# using loop
j = 0
for i in test_dict:
    if (j == 1):
        print('2nd key using loop : ' + i)
    j = j + 1

# accessing 2nd element using keys()
print('2nd key using keys() : ' + test_dict.keys()[1])
      
output:
TypeError: 'dict_keys' object is not subscriptable
2nd key using loop : for





