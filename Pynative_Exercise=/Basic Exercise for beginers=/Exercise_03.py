'''Practice Problem:
 Display only those characters which are present at an even index number in given string.'''
# Given Input: String: "pynative"
String = "pynative"
word=String[::2]
for i in word:
    print(i)
