#Practice Problem: Create a function that takes a string and returns a count of
#how many times each character appears. Ignore spaces and make it case-insensitive.
text = "Python Programming"
D={}
count=0
for i in text.replace(" ","").lower():
    if i in D:
        D[i]+=1
    else:
        D[i]=1
        
print(D)    