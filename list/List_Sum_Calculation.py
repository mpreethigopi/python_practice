"""2. List Sum Calculation
Problem: Write a Python program to calculate the sum of all elements in a given list.
Example:
python
Copy code
input_list = [1, 2, 3, 4, 5]
# Expected Output: 15"""

input_list = [1, 2, 3, 4, 5]
y=0
for x in input_list:
    y += x
print(y)

output=sum(input_list)
print(output)