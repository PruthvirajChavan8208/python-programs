'''Practice Problem:
 Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.'''

#Method 1
# num=int(input("Enter the Number for Factorail"))
# fact=1
# for i in range(5,1,-1):
#     fact=i*fact
# print(f" Factorail of {num} is:{fact}")
#Method 2
def factorail(num):
    if num!=0:
        return num * factorail(num-1)
    else:
        return 1
print(f"Factorial is:{factorail(5)}")

