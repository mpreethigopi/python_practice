#12.	Accept a five digit number as input and print the sum of its digits as output.

digit=0
i=1
no_digit=int(input("Enter the no.of digit to calculate: "))

while i <=no_digit:
    digit_no=int(input(f"Enter the digit{i}: "))
    digit=digit+digit_no
    i=i+1
print("The sum of its digit is:", digit)
    
