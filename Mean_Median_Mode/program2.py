data1=[85,90,76,92,88,79,95,85,87,91,83,77,84,90,86,45]

#mean 
length=len(data1)
sum1=sum(data1)
mean=sum1/length

print("Mean is :", mean)

#Median

data1.sort()
print(data1) 

if length%2!=0:
    index=int((length+1)/2)
    median=data1[index-1]
    print("Median for odd:", median)
else:
    index1=int(length//2)-1
    index2=int(((length/2)))
    median1=data1[index1]
    median2=data1[index2]
    print(median1,median2)
    median=((median1+median2)/2)
    print("Median for even :",median)

#Mode:
i=0
j=1
if i<16:
    if data1[i]==data1[j]:
        print(f"data{i}",data1[i])
        print(f"data{j}",data1[j])
    j=j+1
    i=i+1

