"""3.	Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers."""

num=input("Enter the sequence of five single digit numbers seperated by commas: ")
num1=num.split(",")
print(num1)
prod_var=1

for i in num1:    
    prod_var=prod_var*int(i)
print(f"The product of all five numbers is: {prod_var}")