#List Comprehensions: Write a Python program using list comprehension to generate a list of the squares of the first 10 natural numbers.
#python
# Expected Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i=1
j=10

"""while i<=j:
    k=i*i
   
    i += 1
    print(k)
"""
list1=[i*i for i in range(1,11)]
print(list1)
    