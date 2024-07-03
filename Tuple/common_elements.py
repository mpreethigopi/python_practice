"""5. Find Common Elements in Tuples
Write a Python program to find common elements between two tuples.

Example:

python
Copy code
# Input: t1 = (1, 2, 3, 4), t2 = (3, 4, 5, 6)
# Output: (3, 4)"""

t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

t1=set(t1)
t2=set(t2)
t3=t1&t2
print(t3)