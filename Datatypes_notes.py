#String - str immutable 



a="this is the value of. HHHHHHHH"
print("string of a:", a)
print("Type of a:", type(a))
print("Lenght of a:",len(a)) #to find the length of a characters 
print(a.count("i")) # to count the characters present within the value a
print(a.capitalize()) #makes the first chara only in uppercase and rest in lower case
print(a.upper())#makes the character in uppercase
print(a.lower())#makes the character in lowercase
a1=a.upper()
print(a1)
print(a.partition("t")) #types(before partition,char partition, after partition)
print(a.split("H"))#it will split the character but omit the character

#if the built-in function starts with IS it will display in the True or False

print(a.title()) #it will display all the first character in upper case in a word


#Arithmetic Operator
a,b="P","g"
print(a+b) #concardination

print(a*5) #it will display the a value 5 times

"""
string+string - success eg:"a"+"90"
str_int - error eg: lp+7
int +int - success eg:7+8
"""

#fstring - to display the text with in the screenview
san="""Google was founded on September 4, 1998, by American 
computer scientists Larry Page and Sergey Brin while they were 
PhD students at Stanford University in California. Together, 
they own about 14% of its publicly listed shares and control 56% of 
its stockholder voting power through super-voting stock. The company"""

#Escape charaters:
#\n - new line
print("hellow \nthis my \n new line")
print("hellow \\new line")
#\t - tab space
print("hellow \tthis my \tnew line")

vscode="features \"support\" code"
print (vscode)

credo="we can\'t take this"
print(credo)

#str -->order(indexing, slicing)

#+ve indexing starts from 0 
#-ve indexing starts from -1
str1="this iss the right."
     #01234567......   -      +ve indexing
#...............-5-4-3-2-1 - -ve indexing

str=[3,str1]
print(str1[0])
print(str1[-1]) #- -1 and18 both will display the same output
print(str1[18])

#Slicing
#slicing [start:stop(n+1):step] - step - it will skip that particular char
#+Ve slicing
print("slicing starts")
print(str1[0:22])
print(str1[3:6])
print(str1[0:12:2])
print(str1[ :6])
print(str1[4: ])
print(str1[ : ])


#-ve slicing:
print("-veslicing starts")
slic="clicing"
print (slic[-7:-1])
print(slic[-1:-7])
print(slic[-7: ])

