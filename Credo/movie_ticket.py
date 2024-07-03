show_type = input("Enter the show type :")
show_category = input("Enter the show category:")

if(show_type=="Prime" and show_category =="A"):
	print("Total price of ticket is Rs:240")
	
elif show_type=="Prime" and show_category =="B":
	print("Total price of ticket is Rs:200")
	
elif(show_type=="Base" and show_category =="C"):
	print("Total price of ticket is Rs:180")
	
elif(show_type=="Base" and show_category =="D"):
		print("Total price of ticket is Rs:160")

elif(show_type=="Budget" and show_category =="E"):
	print("Total price of budget ticket is Rs.60")
	
else:
	print("Kindly enter the valid option")
	



