"""15.	Accept a string as input and print the vowels present in the string in alphabetical order. If the string doesn't 
contain any vowels, then print the string none as output. Each vowel that appears in the input string 
— irrespective of its case — should appear just once in lower case in the output"""

string =str(input("Enter the string: ")).lower()


string1=[]

for each_char in string:
    #print(each_char)
    if ((each_char=="a" or each_char=="e" or each_char=="i" 
         or each_char=="o"or each_char=="u")):
        string1.append(each_char)
        remove_duplicate=set(string1)
        list_sort=list(remove_duplicate)
        list_sort.sort()
      

if len(string1)==0:
    print("None")
else:    
    
    print(list_sort)
    



       
        

