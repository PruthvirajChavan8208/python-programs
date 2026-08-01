'''Practice Problem: Given a list of numbers, create a new list where each element 
is the sum of all elements from the original list up to that position'''
a=[1, 2, 3, 4]
s=0
b=[]
for i in a:
    s=s+i
    b.append(s)
print(b)
