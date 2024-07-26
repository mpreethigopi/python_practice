#9.	Accept two integers as input and print their sum as output.

def sum(a,b):
    c=a+b
    return c

a=int(input("Enter the value for 'a': "))
b= int(input("Enter the value for 'b': "))
print(f"The sum of two integers {a},{b} is:",sum(a,b))