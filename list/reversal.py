"""5. List Reversal
Problem: Write a Python program to reverse the order of elements in a given list.
Example:
python
Copy code
input_list = [1, 2, 3, 4, 5]
# Expected Output: [5, 4, 3, 2, 1]"""

input_list = [1, 2, 3, 4, 5]
input_list.reverse()
print(input_list)

print(list(reversed(input_list)))