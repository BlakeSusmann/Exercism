"""Collatz Conjecture Count Measure Function

Collatz Conjecture - with any positive integer 
if even divide by 2 
if odd mulitiply by 3 and add 1
All positive integers will return to 1

Function to process the Collatz Conjecture and Count the Steps
of process for a positive integer back to 1
"""

def steps(number):
    """Calculates how many steps the collatz conjecture takes with an 
    inputed positive integer to return to 1. Function also throws 
    a 'raise' 'exception' 'ValueError' 'only positive integers are alllowed'

    param number: positive integer - the number selected to for
    the collatz conjecture function
    return: int num - variable name 'step_count'

    Function raises value error if needed for 0 and negative numbers inputed 
    and returns number of 'steps_count' for positive integers derieved from
    funcntion Collatz Conjecture  3x + 1 and 3n - 1
    """
    step_count = 0
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number > 1:
        if number % 2 == 0:
            step_count += 1
            number =  number / 2
        elif number % 2 == 1:
            step_count += 1
            number = (number * 3) + 1
    return step_count
        
        
        
