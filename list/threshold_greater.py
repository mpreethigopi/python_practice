"""5. List Elements Above Threshold
Problem: Write a Python program to get all elements in a list that are greater than a specified threshold.
Example:

python
Copy code
input_list = [10, 20, 30, 40, 50]
threshold = 25
# Expected Output: [30, 40, 50]"""

input_list = [10, 20, 30, 40, 50]
threshold = 25

li=[x for x in input_list if x > threshold]
print(li)


