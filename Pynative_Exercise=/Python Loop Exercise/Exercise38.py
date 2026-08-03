'''Practice Problem: Write a program to calculate the sum of the series 2 + 22 + 222 + 2222 + …. up to N terms. For example, 
if n=5, the series is 2 + 22 + 222 + 2222 + 22222.'''
number_of_terms = 5
start=2
sum=0
for i in range(5):
    sum=sum+start
    start= start*10 + 2
print(sum)
