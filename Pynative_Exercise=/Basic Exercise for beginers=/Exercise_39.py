'''Practice Problem: 
Write a script that opens an existing .txt file and counts the total number of words it contains.'''

try:
    with open('Exe_39.txt','r') as file:
        content=file.read()
        word=content.split()
        count=len(word)
        print(f'The File has:{count} words')
except FileNotFoundError:
    print('Error file not Found!')