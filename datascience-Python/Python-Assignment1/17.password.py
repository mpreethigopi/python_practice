"""17.	Accept a string as input. Your task is to determine if the input string is a valid password or not. 
For a string to be a valid password, it must satisfy all the conditions given below:
(1) It should have at least 8 and at most 32 characters
(2) It should start with an uppercase or lowercase letter
(3) It should not have any of these characters: '/' '\' =' ' "
(4) It should not have spaces
It could have any character that is not mentioned in the list of characters to be avoided (points 3 and 4). 
Output True if the string forms a valid password and False otherwise.
.."""

pwd=str(input("Enter the string:"))

length=len(pwd)
space_count=pwd.count(" ")

if length<8 or length>32:
    print("False")
elif space_count>0:
    print("False")
elif not (pwd[0].islower() or pwd[0].isupper()):
    print("False")

else:
    print("True")


