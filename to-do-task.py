def view_todo_list(task):
    print("Your To-Do List:")
    print(task)


def add_task(taska):
    task=input("Enter the task you want to add: ")
    print(f"Task '{task}' has been added to the task.")

    return task

def remove_task():
    task=int(input("Enter the task number you want to remove: "))
    
    print(f"Task '{task}' has been removed from the list.")

def main():
    taska=[]
    while True:
        print("To-Do List Menu:")
        print("1. View To-Do List")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Exit")

        choice=int(input("Enter your choice(1-4): "))

        if(choice==1):
            view_todo_list(task)

        elif choice==2:
            add_task(taska)
            print(task)
        
        elif choice==3:
            remove_task()
        
        elif choice==4:
            print("Exiting the application. Goodbye!")
            break

if __name__ == "__main__":
    main()