"""4. List Intersection
Problem: Write a Python program to find the intersection of two lists.
Example:

python
Copy code
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# Expected Output: [4, 5]"""
li=[]
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
for x in list1:
    for y in list2:
        if x==y:
            li.append(x)
print(li)
         
        
