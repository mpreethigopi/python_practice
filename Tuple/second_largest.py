"""1. Find the Second Largest Element in a Tuple
Write a Python program to find the second largest element in a given tuple.

Example:

python
Copy code
# Input: t = (5, 3, 9, 1, 7)
# Output: 7"""

t = (1, 2)
t1=list(t)
t1.sort()
t1.reverse()
print(t1[1])
t2=tuple(t1)
print(t2[1])