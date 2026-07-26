'''Practice Problem: 
Write a function called exponent(base, exp) that returns an integer value of the base raised to the
 power of the exponent.'''

def base_raise_to(base,exp):
    result=1
    for i in range(exp):
        result=result*base
    print(f'{base} raise to power{exp} is:{result}')
base_raise_to(2,5)
base_raise_to(6,3)