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
