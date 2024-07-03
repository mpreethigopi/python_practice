def add_student(nostud):
    grade={}
    for i in range(nostud):
        name=str(input("Enter the name of the student:"))
        age=int(input("Enter the age for the student:"))
        liofcourses=str(input("Enter the courses selected by the student:"))
        print(name, age, liofcourses)
    


nostud=int(input("Enter the number of student needs to be updated in the system:"))
add_student(nostud)