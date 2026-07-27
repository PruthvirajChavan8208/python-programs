'''Practice Problem: 
Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.'''
a=[]

for num in range(2,21):
    if num>1:
        for i in range(2,num):
            if (num%i) ==0:
                print(num,'is not prime no')
                break
        else:
                print(num,'is a prime no')
                a.append(num)
                
                
    else:
        print(num,'is not a prime no')
print(a)
print(a[::2])

