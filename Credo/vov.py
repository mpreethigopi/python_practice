"""15.	Accept a string as input and print the vowels present in the string in alphabetical order. If the string doesn't 
contain any vowels, then print the string none as output. Each vowel that appears in the input string 
— irrespective of its case — should appear just once in lower case in the output"""

string =str(input("Enter the string: ")).lower()


string1=set()
vowels={"a","e","i","o","u"}

for each_char in string:
    if each_char in vowels:
        string1.add(each_char)
        y=sorted(string1)
print(y)