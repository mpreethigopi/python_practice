"""List Cumulative Sum:

Problem: Write a Python program to create a new list where each element is the cumulative sum of the elements of the original list.
Example:
python
Copy code
input_list = [1, 2, 3, 4, 5]
# Expected Output: [1, 3, 6, 10, 15]"""
i=0
input_list = [1, 2, 3, 4, 5]
for x in range(5):
    for y in x:
        y=y+x
    

print(x)




