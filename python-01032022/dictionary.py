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
Dictionary popitem()
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
Exp 1:





