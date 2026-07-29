'''Practice Problem: 
Write a program to capitalize the first letter of each word in a given string without using the built-in
 .title() method.'''
text = "hello world from python"
#print(text.title())
a=[]
word=text.split()
for i in word:
    a.append(i.capitalize())

result=' '.join(a)
print(result)