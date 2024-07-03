"""List Duplication Removal:

Problem: Write a Python program to remove duplicates from a list while maintaining the order of elements.
Example:
python
Copy code
input_list = [1, 2, 2, 3, 4, 4, 5]
# Expected Output: [1, 2, 3, 4, 5]"""

input_list = [1, 2, 2, 3, 4, 4, 5]
s1=set(input_list)
print(list(s1))