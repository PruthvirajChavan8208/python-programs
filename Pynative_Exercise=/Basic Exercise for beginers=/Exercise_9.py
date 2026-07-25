'''Practice Problem: 
Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.'''
sentence = "Learning Python is fun!"
vowels=['a','e','i','o','u']
count=0
for i in  sentence:
    if i in vowels:
        count+=1
print("The no of vowel is",count)
