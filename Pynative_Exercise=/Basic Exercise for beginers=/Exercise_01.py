# Practice Problem: 
# Write a Python function that accepts two integer numbers.If the product of the two numbers is less
#  than or equal to 1000,return their product; otherwise, return their sum.

# Given Input:

# Case 1: number1 = 20, number2 = 30
# Case 2: number1 = 40, number2 = 30
# Expected Output:

# The result is 600
# The result is 70

def multiplication_or_sum(num1,num2):
    product=num1 * num2
    sum=num1+num2
    if product >=1000:
        return sum
    else:
        return product
result=multiplication_or_sum(20,30)
print('The result is:',result)
result=multiplication_or_sum(40,30)
print('The result is:',result)
