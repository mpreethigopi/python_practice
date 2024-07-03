"""4. List of Unique Elements
Problem: Write a Python program to get a list of unique elements from a given list of integers.
Example:
python
Copy code
input_list = [1, 2, 2, 3, 4, 4, 5]
# Expected Output: [1, 2, 3, 4, 5]"""

input_list = [1, 2, 2, 3, 4, 4, 5]
s1=set(input_list)
print(list(s1))


