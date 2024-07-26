"""2.	Accept the date in DD-MM-YYYY format as input and print the year as output."""



def display_year():
    date=input("Enter the date in 'DD-MM-YYYY' format: ")
    split_date=date.split("-")
    return split_date[2]

print("The year is: ",display_year())