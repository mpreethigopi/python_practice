def add_student(students):
    # Implement the function to add a new student
    no_stud=int(input("Enter the no.of student to be registered: "))
    print("\n")
    print("Adding student to the system")
    print("****************************")
   
    for i in range(no_stud):
            stud_id=input(f"Enter the student ID for the student {i+1}: ")
            stud_name=input("Enter the student name: ")
            stud_age=int(input(f"Enter the age for the student {stud_name}: "))
            stud_grade_math=int(input(f"Enter the Maths grade for the student {stud_name}: "))
            stud_grade_science=int(input(f"Enter the Science grade for the student {stud_name}: "))
            stud_grade_english=int(input(f"Enter the English grade for the student {stud_name}: "))  
            print("\n")      
            add_stud = {
                stud_id:{
                    "name":stud_name, 
                    "age": stud_age,
                    "grade":{
                        "math": stud_grade_math,
                        "science":stud_grade_science,
                        "english":stud_grade_english
                        }
                    }
                }
            students.update(add_stud)
    return students
    


def remove_student(students):
    # Implement the function to remove an existing student
    print("The available students in the system are ", students)
    stud_id=input("Enter the student id which needs to be removed: ")
    
    if stud_id in students:
            del students[stud_id]
            print(f"Student {stud_id} removed from the system")
            print("Current student present in the system", students)
    else:
            print("Enter the valid student ID")

   

def update_student(students):
    stud_id=input("Enter the student id where the information needs to be updated: ")
    
    if stud_id in students:
                print("Enter the updated details for the student")
                stud_name_u=input("Enter the updated name: ")
                stud_age_u=int(input("Enter the updated age: "))
                stud_grade_m_u=int(input("Enter the updated math mark: "))
                stud_grade_s_u=int(input("Enter the updated science mark: "))
                stud_grade_e_u=int(input("Enter the updated english mark: "))
                print(f"Updated details for the student {stud_id}")
                students[stud_id]={
                    "name":stud_name_u,
                    "age":stud_age_u,
                    "grade":{
                        "math":stud_grade_m_u,
                        "science": stud_grade_s_u,
                        "english": stud_grade_e_u
                    }
                }
                
                print(f"{stud_id}:{students[stud_id]}")       
    else: 
        print("An error occured")

def display_student(students):
    #Display the details of a student using their unique ID
    print("The available students in the system are ", students)
    stud_id=input("Enter the student id where the information needs to be displayed: ")
   
    if stud_id in students:
            print(f"The details of the student {stud_id} are:")
            print(f"{stud_id}:{students[stud_id]}")

    else:
            print("Enter the valid student ID")



def display_all_students(students):
    # Implement the function to display all students' information

        if len(students)>0:
            print("The available student in the system are :", students)
        else:
                print("No student available in the system")


def calculate_average_grade(students):
    # Implement the function to calculate the average grade of a student

    stud_id=input("Etner the student ID which the average needs to be calculated: ")
    if stud_id in students:
        # print(students, "student details")
            """math_grade=students[stud_id]["grade"]["math"]
            science_grade=students[stud_id]["grade"]["science"]
            english_grade=students[stud_id]["grade"]["english"]
            average=(math_grade+science_grade+english_grade)/3"""
            grades=students[stud_id]["grades"]
            average=sum(grades.values())/len(grades)
            print("The average grade of the student is: ", average)
    else:
        print("Enter a valid student ID")
def main():
    students = {}
    
    while True:
        print("Student Management System")
        print("1. Add a Student")
        print("2. Remove a Student")
        print("3. Update Student Information")
        print("4. Display Student Information")
        print("5. Display All Students")
        print("6. Calculate Average Grade")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_student(students)
            print(students)
        elif choice == 2:
            remove_student(students)
        elif choice == 3:
            update_student(students)
        elif choice == 4:
            display_student(students)
        elif choice == 5:
            display_all_students(students)
        elif choice == 6:
            calculate_average_grade(students)
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()