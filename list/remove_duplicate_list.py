"""List Manipulation: Write a Python program to remove duplicates from a list while preserving the order.

python
Copy code
input_list = [1, 2, 3, 1, 2, 3, 4, 5]
# Expected Output: [1, 2, 3, 4, 5]"""

input_list = [1, 2, 3, 1, 2, 3, 4, 5]

print(set(input_list))
seen=set()
result=[]

for i in input_list:
 
    if i not in seen:
        seen.add(i)
        result.append(i)

print(result)







    
    

