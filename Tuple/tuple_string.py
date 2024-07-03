"""2. Convert a Tuple to a String
Write a Python program to convert a tuple of characters into a string.

Example:

python
Copy code
# Input: t = ('h', 'e', 'l', 'l', 'o')
# Output: "hello" """
y=""
t = ('h', 'e', 'l', 'l', 'o')
for x in t:
    y=y+x
print(y)

"""3. Remove Duplicates from a Tuple
Write a Python program to remove duplicate elements from a tuple and return a tuple with unique elements.

Example:

python
Copy code
# Input: t = (1, 2, 3, 2, 4, 1, 5)
# Output: (1, 2, 3, 4, 5)"""

t = (1, 2, 3, 2, 4, 1, 5)
t1=set(t)

t=tuple(t1)
print(t)

"""
4. Reverse a Tuple
Write a Python program to reverse the elements of a tuple.

Example:

python
Copy code
# Input: t = (1, 2, 3, 4, 5)
# Output: (5, 4, 3, 2, 1)"""
t = (1, 2, 3, 4, 5)

t1=list(reversed(t))
print(tuple(t1))

"""
5. Tuple of Tuples to a Single Tuple
Write a Python program to convert a tuple of tuples into a single tuple.

Example:

python
Copy code
# Input: t = ((1, 2), (3, 4), (5, 6))
# Output: (1, 2, 3, 4, 5, 6)
Detailed Descriptions:
"""

t = ((1, 2), (3, 4), (5, 6))
for x in t:
    for y in x:
        print(tuple(y))




