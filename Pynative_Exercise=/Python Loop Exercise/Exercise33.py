#Practice Problem: Write a program to count the frequency of each word in a given string
text = "apple banana apple orange banana apple"
words=text.split()
a={}
for i in words:
    if i in a:
        a[i]+=1
    else:
        a[i] = 1   
print (a)       
        
    
