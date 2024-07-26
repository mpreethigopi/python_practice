"""EvenOdd is a tech startup. Each employee at the startup is given an employee id which is a unique positive integer. 
On one warm Sunday evening, five employees of the company come together for a meeting and sit at a circular table:
The employees follow a strange convention. They will continue the meeting only if the following condition is satisfied.
The sum of the employee-ids of every pair of adjacent employees at the table must be an even number.
They are so lazy that they won't move around to satisfy the above condition. If the current seating plan doesn't satisfy the condition,
 the meeting will be canceled. You are given the employee-id of all five employees. Your task is to decide if the meeting happened or not.
The input will be five lined, each line containing an integer. The 
i^{th}
i
th
line will have the employee-id of 
Ei
Ei. The output will be a single line containing one of these two strings: 
"""

eid=[10,2,4,6,7]
for i in range(len(eid)):
    if i < len(eid):
        if (eid[i]+eid[i+1])%2!=0:
            print("No Meeting")
            break
        if(eid[i]+eid[0])%2!=0:
            print("No Meeting")
    else:
         print("Yes Meeting")
    