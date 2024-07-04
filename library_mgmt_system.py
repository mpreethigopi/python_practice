#Add book to the library
def add_book(lib_book):
    no_book=int(input("Enter the no.of book to be added: "))
    print("Adding the book into the library")
    print("________________________________")
    for i in range(no_book):
       y=i+1
       title=input(f"Enter the book{y} title: ") 
       author=input(f"Enter the author for the book{y}: ")
       genre=input(f"Enter the genre for book{y}: ")
       availability=input(f"Enter the book{y} availability: ")
       print("\n")
       book={f"lib{y}":[title,author,genre,availability]}
       lib_book.update(book)
    return lib_book

#Remove book from the library
def remove_book(lib_book):
     book_id=input("Enter the library book id which needs to be removed: ")
     if book_id in lib_book:
          print("removed book details: ", {book_id:lib_book[book_id]})
          del lib_book[book_id]
          print("Book removed from the library")
          print("Current book present in the library", lib_book)
     else:
          print("The book id is not available in the library")

#Displays confirmation message with the updated status of the book
def checkout_book(lib_book):
    book_id=input("Enter the library book id for checkout: ")
    if book_id in lib_book:
            print("Book id is: ",book_id)
            value=lib_book[book_id]
            if len(value)>=4:
                value[3]="Check out"
                print(f"Updated status of the book {book_id}:", {book_id:value})
                print("\n")
            print("Current status of all the book:")
            print(lib_book)

    else:
        print("The book ID does not exist or is already checked out")  

#Return book to the library
def return_book(lib_book):
    book_id=input("Enter the library book id for return: ")
    if book_id in lib_book:
         print("The book which needs to be returned is: ", book_id)
         value=lib_book[book_id]
         if len(value)>=4:
              value[3]="Yes"
         print("Book is returned in the library")
         print("\bUpdated library book:")
         print(lib_book)
    else:
         print("The book ID does not exist or is not checked out.")

               

#Display book information for the specified book id
def display_book(lib_book):
    book_id=input("Enter the library book id: ")
    ##print("Inside display book loop",lib_book)
    
    if book_id in lib_book:               
            print(f"The book information for the specified id {book_id} is", lib_book[book_id])
            print("The book id is: ",book_id)
            value = lib_book[book_id]
            
            print("The book title is: ",value[0])
            print("The author for the book is: ",value[1])
            print("The Genre for the book is: ",value[2])
            print("The availability for the book is ",value[3])
        
    else:
            print("The book ID does not exist or is already checked out")

"""#Displays a list of books in that genre 
def search_genre(lib_book):
     book_genre=input("Enter a genre to search: ")
     for book_genre in lib_book:
          print(lib_book)
          print(book_genre)
          value=lib_book.values[1]
          print(value)"""
     
#To display all books that are currently available
def display_all_book(lib_book):
    if len(lib_book)>0:
          print("Below books are currently available in the library")
          print(lib_book)
    else:
         print("Books are not available in the system")
          


          
     
     

#Main program
print("**************************")
print("Library Management System")
print("**************************\n")
print("Select one value from below:")
print("1. Add books to library")
print("2. Remove books to library")
print("3. Checkout books to library")
print("4. Return the book to library")
print("5. Display Book Information for the specified ID")
print("6. Search by Genre")
print("7. To display all books that are currently available")
print("\n")

#Selection criteria
library_value=int(input("Select one value from above: "))
library_book={}
if library_value==1:
    add_book(library_book)
    print(library_book)
elif library_value==2:
     add_book(library_book)
     remove_book(library_book)
elif library_value==3:
     add_book(library_book)
     checkout_book(library_book)
elif library_value==4:
     add_book(library_book)
     return_book(library_book)
elif library_value==5:
    add_book(library_book)
    display_book(library_book)
elif library_value==6:
    add_book(library_book)
    #search_genre(library_book)
elif library_value==7:
    add_book(library_book)
    display_all_book(library_book)
    

else:
    print("Select the value from 1 to 6")