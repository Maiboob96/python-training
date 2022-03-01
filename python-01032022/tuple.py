            Python Tuple Methods
  __________________________________________________

  Types of Tuple methods
  
  1) Tuple Count()
  2) Tuple Index()
  
  
  (1) Count method():
  -----------------------------------------------------
  
The count() method of Tuple returns the number of times the given element appears in the tuple.
Syntax:
       tuple.count(element)
 
count() Parameters
The count() method takes a single argument:

element - the element to be counted


Return value from count()
The count() method returns the number of times element appears in the tuple.

Exp 1 : using of tuple count
  
# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)

Exm 2: Count List and Tuple Elements Inside Tuple
  
# random tuple
random = ('a', ('a', 'b'), ('a', 'b'), [3, 4])

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)

Exm 3: 
# Creating tuples
Tuple = (0, 1, (2, 3), (2, 3), 1,
         [3, 2], 'geeks', (0,))

# count the appearance of (2, 3)
res = Tuple.count((2, 3))
print('Count of (2, 3) in Tuple is:', res)

# count the appearance of [3, 2]
res = Tuple.count([3, 2])
print('Count of [3, 2] in Tuple is:', res)



(2)  Index() Method :
 ---------------------------------------------
The index() method returns the index of the specified element in the tuple.
Syntax:
     tuple.index(element, start, end)
 

Tuple index() parameters
The tuple index() method can take a maximum of three arguments:

element - the element to be searched
start (optional) - start searching from this index
end (optional) - search the element up to this index


Return Value from Tuple index()
The index() method returns the index of the given element in the tuple.
If the element is not found, a ValueError exception is raised.

Programs:
  
Exm 1: index of element
  
# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

Exm 2: Index of the Element not Present in the Tuple
# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'u')

# index of'p' is vowels
index = vowels.index('p')
print('The index of p:', index)

output: ValueError: tuple.index(x): x not in tuple
      
      

print('The index of i:', index) 

    
