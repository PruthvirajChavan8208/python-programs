'''Practice Problem: Write a program that takes a year as input and determines if it is a leap year.'''
def leap_year(year):
    if (year %4==0 and year % 100 !=0) or (year % 400 == 0):
        print(f'{year} is leap Year')
    else:
        print(f'{year} is not a leap year')
leap_year(2000)
leap_year(400)
leap_year(1700)
leap_year(2012)
leap_year(2017)