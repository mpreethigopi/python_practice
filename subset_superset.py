"""Set Subset and Superset:

Problem: Write a Python program to check if one set is a subset or superset of another set.
Example:
python
Copy code
set1 = {1, 2}
set2 = {1, 2, 3, 4}
# Expected Output: True (set1 is a subset of set2), False (set2 is a subset of set1)"""

set1 = {1, 2}
set2 = {1, 2, 3, 4}
#subset:
set3=set1<=set2
set4=set1.issubset(set2)
print(set3)
print(set4)

#superset

set5=set2>=set1
set6=set2.issuperset(set1)
print(set5)
print(set6)