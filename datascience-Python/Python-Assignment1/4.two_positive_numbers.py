"""4.	Accept two positive integers x and y as input. Print the number of digits in xy."""

x=int(input("Enter the integer1: "))
y=int(input("Enter the integer2: "))
result=1
for i in range(y):
    result=result*x
print("The result is", result)
no_digits=len(str(result))
print("No.of digits:", no_digits)