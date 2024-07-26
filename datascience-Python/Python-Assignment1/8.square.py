#8.	Accept an integer as input and print its square as output.
#Note: Do not worry about the \n that you observe in the expected output. It can be ignored.

i=int(input("Enter the integer to find the square: "))

if i<=0:
    print("Enter the valid positive integer")
else:
    sq=i*i
    print(f"The square for the number '{i}' is: ", sq)


