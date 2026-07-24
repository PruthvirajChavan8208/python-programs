'''Practice Problem:
 Write a function to remove characters from a string starting from index 0 up to n and return a new string.'''

def string_slicing(String,num):
    word=String[num:]
    return word
print(string_slicing('pynative',4))
print(string_slicing('pynative',2))