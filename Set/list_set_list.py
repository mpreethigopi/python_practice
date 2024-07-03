"""Set Conversion:

Problem: Write a Python program to convert a list to a set and a set to a list.
Example:
python
Copy code
input_list = [1, 2, 2, 3, 4]
# Expected Output (List to Set): {1, 2, 3, 4}
input_set = {1, 2, 3, 4}
# Expected Output (Set to List): [1, 2, 3, 4]"""

input_list = [1, 2, 2, 3, 4]

st=set(input_list)
print(st)
li=list(st)
print(li)