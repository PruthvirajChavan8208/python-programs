'''Practice Problem: 
Given a Python list, use a loop to print only the elements that are located at odd index positions 
(index 1, 3, 5, etc.).'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
a=[]
# print(my_list[1::2])
for i in range(1,len(my_list),2):
    a.append(my_list[i])
print(a)
