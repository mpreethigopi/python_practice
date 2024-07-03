"""Set Symmetric Difference:

Problem: Write a Python program to find the symmetric difference between two sets.
Example:
python
Copy code
set1 = {1, 2, 3}
set2 = {2, 3, 4}
# Expected Output: {1, 4}"""

set1 = {1, 2, 3}
set2 = {2, 3, 4}


set3=set1.symmetric_difference(set2)
print(set3)

set1.symmetric_difference_update(set2)
print(set1)
