"""Problem: Write a Python program to remove specific elements from a set.
Example:
python
Copy code
set1 = {1, 2, 3, 4, 5}
elements_to_remove = {2, 4}
# Expected Output: {1, 3, 5}"""

set1 = {1, 2, 3, 4, 5}
output={x for x in set1 if x%2!=0}
print(output)

set1 = {1, 2, 3, 4, 5}
elements_to_remove = {2, 4}  
output1={y for y in set1 if y not in elements_to_remove}
print(output1)