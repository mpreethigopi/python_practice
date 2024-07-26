"""7.	Print the following pattern.
*
**
***
****
*****
There are no spaces between consecutive stars. There are no spaces at the end of each line.
"""

rows=5 
for i in range(1, rows+1):
    #print("e")
    for j in range(i):
        print("*", end="")
    print()
