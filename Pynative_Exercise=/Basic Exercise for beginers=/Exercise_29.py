'''Practice Problem: 
Create a list of 5 words. 
Write a loop that iterates through the list and prints each word alongside its character count.'''
words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for i in words:
    a=len(i)
    print(f'{i} - {a}',end='\t')