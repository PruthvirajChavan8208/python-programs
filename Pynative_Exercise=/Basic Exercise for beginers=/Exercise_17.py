'''Practice Problem: 
Create a new list from two given lists such that the new list contains odd numbers
 from the first list and even numbers from the second list.'''
# Expected Output: [25, 35, 40, 60, 90]

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

op=[]
for i in list1:
    if i % 2 !=0:
        op.append(i)
for j in list2:
    if j % 2 == 0:
        op.append(j)
print(op)
