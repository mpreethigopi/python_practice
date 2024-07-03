"""List Element Squaring:

Problem: Write a Python program to create a new list that contains the squares of all elements in the original list.
Example:
python
Copy code
input_list = [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]"""

input_list = [1, 2, 3, 4, 5]

sq=[]
for i in input_list:
    x=i*i
   
    sq.append(x)
print(sq)


