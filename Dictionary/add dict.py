"""Dictionary Operations: Write a Python program to merge two dictionaries, adding values for common keys.

python
Copy code
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}
# Expected Output: {'a': 400, 'b': 400, 'c': 300, 'd': 400}"""

"""dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}


key1=dict1.keys()
print(key1)
key2=dict2.keys()
print(key2)

key3=dict1.items()
print(key3)
len1=len(dict1.keys())
print(type(len1))
i=0
for  i in len1:
   if dict1.keys()==dict2.keys():
      values3= dict1.values()+dict2.values()
      print(values3)
else:
   print("oo")
"""


i=5 #here i holds integer value

j=str(i) #here i value is converted to string which is int is converted to string
print(type(j))