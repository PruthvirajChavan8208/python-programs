#Practice Problem: Given a list of integers, move all even numbers to the beginning of the list and al
#l odd numbers to the end.
num=[1, 2, 3, 4, 5, 6]
a=[]
b=[]
for i in num:
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)
result=a+b
print(result)        