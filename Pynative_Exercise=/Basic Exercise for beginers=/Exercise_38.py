'''Practice Problem: 
Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, 
and then reads that file back to display the contents in the console.'''

with open('exe_38_sol.txt','w') as file:
    file.write('Hello, this is my first note.\n')
    file.write('Python file handling is simple.\n')
    file.write('End of file.\n')

with open('exe_38_sol.txt','r') as file:
    content=file.read()
print(content)