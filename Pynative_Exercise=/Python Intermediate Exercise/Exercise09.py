a=[1, 2, 2, 3, 1, 4, 2]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)        