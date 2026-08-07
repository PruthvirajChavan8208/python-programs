#Practice Problem: Given a sentence, reverse each individual word within
# the string while maintaining the original word order.
def reverse_string(val):

    words=text.split()
    reversed_word=[word[::-1] for word in words ]
    return " ".join(reversed_word)
text="Python is awesome"
result =reverse_string(text)
print(result)