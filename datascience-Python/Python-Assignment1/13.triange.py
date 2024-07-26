 #13.	Accept three positive integers as input and check if they form the sides of a right triangle. Print YES if they form one, 
 # and NO if they do not. The input will have three lines, with one integer on each line. 
 # The output should be a single line containing one of these two strings: YES or NO.

a=int(input("Enter the value for a: "))
b=int(input("Enter the value for b: "))
c=int(input("Enter the value for c: "))

a1=a*a
b1=b*b
c1=c*c

if a1+b1==c1:
    print("YES")
else:
    print("NO")
