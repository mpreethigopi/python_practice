"""


def calculate_factorial(number):
    i=fact=1
    while i <= number:
        fact=fact*i
        i+=1
    return fact



number=int(input("Enter the factorial value: "))
output=calculate_factorial(number)
print(output)"""
    

def calculate_factorial(number):
    i=fact=1
    while i<=number:
        fact=fact*i
        i+=1
    return fact

number=int(input("Enter the calculate_factorial: "))  
output=calculate_factorial(number)
print(output)