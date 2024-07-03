"""Nested List: Write a Python program to flatten a nested list structure.

python
Copy code
input_list = [[1, 2, [3, 4]], [5, 6], 7]
# Expected Output: [1, 2, 3, 4, 5, 6, 7]"""

input_list = [[1, 2, [3, 4]], [5, 6],7]
y1=[]
z1=[]
for x in input_list:
        thislist=[x]
        #print(thislist)
        for y in thislist:
                y1.append(y)
                for z in y1:
                        z1.append(z)
            
print(z1)   

  
    