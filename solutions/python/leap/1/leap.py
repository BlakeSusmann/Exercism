"""Functions used in determining (in the Gregorian calendar) if a year is a leap year

Leap years occur only if year is (eveningly) divisible by 4 and not 100 
Or if the year is divisble by 100 and 400.
"""

def leap_year(year):
    """Calculate if leap year is 'true' (or if a year is a leap year 29 days in Feb).

    :param year: int - year (in the gregorian calendar)
    :return: bool - is year a leap year.

    Function that checks if a year is a leap year as an arguement returning true if the year is
    divisible by 4 and not 100 or divisible by 100 and 400 only. 
    """
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)