import math
studs=[]

def add_stud():
    no_stud=int(input("Enter the number of student to be added: "))
    print("Add a new student")

    for i in range(no_stud):
        y=i+1    
        name=input(f"Enter the Student{y} name: ")
        grade=input(f"Enter the Student{y} grade: ")
        stud={f"studid{y}":[name,grade]}
        studs.append(stud)   
       
    list_stud3=studs
    dict1={}
    for j in list_stud3:
        dict1.update(j)
    print("The registered students are",dict1)
    return dict1


def update_grade():
   
    studid_u=input("Enter the Student id for which the grade needs to be updated: ")
    stud_grade_u=input("Enter the Student grade which needs to be updated: ")
    if studid_u in add_student:
        stud_info=add_student[studid_u]        
        stud_info[1]=stud_grade_u
        print("Updated Student details")
        print({studid_u:stud_info})

    print("List of all students with updated grade")
    print(add_student)

def remove_stud():
    studid_u=input("Enter the Student id for which needs to be removed: ")
    if studid_u in add_student:
        print(studid_u)
        add_student.pop(studid_u)
                
    print(add_student)

def high_grade():
    
    print("Highest Grade in the class")
    sec_grade=(x[1] for x in add_student.values())
    high_grade1=max(sec_grade)
    print(high_grade1)
   
def min_grade():
    
    print("Lowest Grade in the class")
    sec_grade=(x[1] for x in add_student.values())
    min_grade1=min(sec_grade)
    print(min_grade1)

add_student=add_stud()
update_grade()
high_grade()
min_grade()
remove_stud()