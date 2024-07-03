"""Problem: Write a Python program to find all pairs of numbers in a list that add up to a given sum.
Example:
python
Copy code
input_list = [1, 2, 3, 4, 5]
target_sum = 5
# Expected Output: [(1, 4), (2, 3)]"""

input_list = [1, 2, 3, 4, 5]
target_sum = 5

for x in input_list:
    if x+x==5:
        print(input_list.append(x))