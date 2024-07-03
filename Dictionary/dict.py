"""Question 2: Merge Dictionaries
Write a program to merge two dictionaries into one. If there are overlapping keys, the values from the second dictionary should overwrite the values from the first dictionary.

Example:

python
Copy code
# Input: dict1 = {'a': 1, 'b': 2}, dict2 = {'b': 3, 'c': 4}
# Output: {'a': 1, 'b': 3, 'c': 4}"""
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict3=dict1&dict2
print(dict3)
