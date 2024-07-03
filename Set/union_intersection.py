"""Set Union and Intersection:

Problem: Write a Python program to find the union and intersection of two sets.
Example:
python
Copy code
set1 = {1, 2, 3}
set2 = {2, 3, 4}
# Expected Output (Union): {1, 2, 3, 4}
# Expected Output (Intersection): {2, 3}"""

set1 = {1, 2, 3}
set2 = {2, 3, 4}
Intersection=set1&set2
print(Intersection)

union=set1|set2
print(union)

