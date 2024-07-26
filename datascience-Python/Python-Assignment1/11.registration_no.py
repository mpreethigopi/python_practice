#11.	Accept the registration number of a vehicle as input and print its state-code as output
dict={
    'AN':"Andaman and Nicobar Islands",
    "AP":"Andhra Pradesh",
    "AR":"Arunachal Pradesh",
    "AS":"Assam",
    "TN":"Tamil Nadu"
    }

reg_no=input("Enter the Registration number of a vehicle: ")
state_code=reg_no.split(" ",2)
#state_code=reg_no[0:2]

for key,value in dict.items():
    state_abbreviation=dict.get(state_code[0])
print(f"The state_code is '{state_code[0]}' and it's abbreviation is '{state_abbreviation}'")