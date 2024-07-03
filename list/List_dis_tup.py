#1. Create a list of names and print the second item.
list=["a",1,23,34,56]
print(list[2])

#2. Create a list of sports and then replace the second item with another sport.
sports=["basketball","Football","Hockey","Chess","Caram"]
sports[1]="Cricket"
print(sports)

#3. Create a list containing numbers and delete the fifth number from the array.
listnumber=[1,2,3,4,5,6,7,8]
del listnumber[4]
print(listnumber)

#4. Create two lists of numbers and merge them.

l1=[0,2,3,4,5]
l2=[5,6,7,8,9]
print(l1+l2)

#5. Create a list of numbers and find the length, minimum, and maximum.
print(len(l1))
print(min(l1))
print(max(l1))

#6. Create a dictionary of students and scores and print out a student’s score.
dic={"stu1":90,"stu2":89,"Stud3":45}
print(dic["stu1"])

#7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
del(dic["stu2"])
print(dic)

#8. Create a dictionary of names and ages and then print out all the keys and values
print(dic.keys)
print(dic.values)

#9. Create a tuple of your favorite movies
tup=("Mov1","Mov2","Mov3","Mov4")

#10. Create a tuple and print all the items from the first to third index.
print(tup[0:3])