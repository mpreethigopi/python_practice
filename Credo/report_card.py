
print("****** REPORT CARD ******")
stud_name=input("Enter the student name: ")
maths_mark=float(input("Enter the mark for Maths subject: "))
science_mark=float(input("Enter the mark for Science subject: "))
social_mark=float(input("Enter the mark for Social subject: "))

total=maths_mark+science_mark+social_mark
avg=(total / 3)


if(maths_mark>=35 and science_mark>=35 and social_mark>=35):
    print(stud_name,"has cleared the exam")
    if(avg==100):
        print("The average mark for this student","is :",avg, "and the grade is A+")
    elif((avg>=90 and avg<=99)):
        print("The average mark for this student","is :",avg, "and the grade is A")
    elif((avg>=80 and avg<=89)):
        print("The average mark for this student","is :",avg, "and the grade is B")
    elif((avg>=70 and avg<=79)):
        print("The average mark for this student","is :",avg, "and the grade is C'")
    elif((avg>=60 and avg<=69)):
        print("The average mark for this student","is :",avg, "and the grade is D")
    elif((avg>=35 and avg<=59)):
        print("The average mark for this student","is :",avg, "and the grade is U")
else:
     print(stud_name,"has failed the exam")
     print("The average mark for this student","is :",avg, "and No Grade is assigned as the student has failed.")

