"""16.	You are given the dates of birth of two persons, not necessarily from the same family. 
Your task is to find the younger of the two. If both of them share the same date of birth, 
then the younger of the two is assumed to be that person whose name comes first in alphabetical order.

The input will have four lines. The first two lines correspond to the first person, 
while the last two lines correspond to the second person. For each person, the first line corresponds to the name and 
the second line corresponds to the date of birth in DD-MM-YYYY format.
Your output should be the name of the younger of the two."""

name1=input("Enter the name of the person 1: ")
dob1_p=input("Enter the Date of Birth (DD-MM-YYYY) for person 1: ")

name2=input("Enter the name of the person 2: ")
dob2_p=input("Enter the Date of Birth (DD-MM-YYYY) for person 2: ")

dob1=dob1_p.split("-")
dob1_date=dob1[0]
dob1_month=dob1[1]
dob1_year=dob1[2]
dob2=dob2_p.split("-")
dob2_date=dob2[0]
dob2_month=dob2[1]
dob2_year=dob2[2]

li_names=[name1,name2]
print(li_names)

if (dob1_year==dob2_year):
    if dob1_month==dob2_month:
        if dob1_date==dob2_date:
            li_names.sort()
            print(li_names[0], "is younger.")
        elif dob1_date>dob2_date:
            print(name2, "is younger.") 
        else:
            print(name1, "is younger.")
    elif dob1_month>dob2_month:
        print(name1, "is younger.")  
    else:
        print(name2, "is younger.") 
elif dob1_year>dob2_year:
    print(name1, "is younger.")
else:
    print(name2, "is younger.")


