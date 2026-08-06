#Practice Problem: Write a single-line list comprehension that takes a list of strings,
# filters out strings shorter than 4 characters, and converts the remaining
 #strings to uppercase.
words = ["apple", "bat", "cherry", "dog", "elderberry"]
filter_words=[i.upper() for i in words if len(i) >=4]
print (filter_words)