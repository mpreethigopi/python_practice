data = [4, 8, 6, 5, 3, 8, 7, 5, 8, 4, 5, 6, 7, 5, 8]

#Mean: Calculate the mean (average) number of books read.#avg=xi/fi

frequency=len(data)
sum1=sum(data)
avg=sum1/frequency
print("Mean: ", avg)


#Median: Determine the median number of books read.
print(dir(data))
data.sort()
print(data)
n=len(data)
print(n)

median=int((n+1)/2)
print("Middle value: ", median)
print("Median is: ", data[median])

