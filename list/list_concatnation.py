"""3. List Concatenation
Problem: Write a Python program to concatenate two lists index-wise.
Example:
python
Copy code
list1 = ["Hello", "Take"]
list2 = ["Dear", "Sir"]
# Expected Output: ["HelloDear", "TakeSir"]"""

list1 = ["Hello", "Take"]
list2 = ["Dear", "Sir"]

len=len(list1)

list3=[]
for x in range(len):
    list3.append(list1[x]+list2[x])
   
print(list3)



