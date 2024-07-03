"""Set Comprehension: Write a Python program using set comprehension to find all the vowels in a given string.

python
Copy code
input_string = "hello world"
# Expected Output: {'e', 'o'}"""

input_string = "hello world"
#set
vol={x for x in input_string if x in 'aeiou'}

print(vol)

#list
listv=[x for x in input_string if x in 'aeiou']
print(listv)

#Dic
dicv={x:x for x in input_string if x in 'aeiou'}
print(dicv)

#Tuple
tuplev=tuple(x for x in input_string if x in 'aeiou')
print(tuplev)