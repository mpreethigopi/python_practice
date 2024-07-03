"""1. List Element Removal
Problem: Write a Python program to remove all even numbers from a given list of integers.
Example:
python
Copy code
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [1, 3, 5, 7, 9]"""

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers=[]
for x in input_list:
   
    if x%2!=0:        
        numbers.append(x)
       
print(numbers)

odd_numbers= [x for x in input_list if x%2!=0]
print(odd_numbers)


import random

colors = ['red', 'blue', 'green', 'yellow']
random_color = random.choice(colors)
print(random_color)









