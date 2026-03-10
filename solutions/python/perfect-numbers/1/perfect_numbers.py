"""Calculates whether a positive integer is perfect, 
abundant, or deficient according Nicomachus and 
the aliquot sum of a number 

aliquot sum is factors of number added up, not including 
the number itsself - if equal sums number is perfect
"""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    #raise value error for non-positive numbers
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')

    #function to call to have a list of factors of a number not including itsself
    #no n+1 leaves last number out of return
    def get_factors(n):
        return [i for i in range(1, n) if n % i == 0]
    #get aliquot sum from 'get_factors' function 
    #check to see if equal to orginal number 
    #defines perfect number if true
    if sum(get_factors(number)) == number:
        return 'perfect'
    #if aliquot sum larger than number number is called abundant return adbundant
    if sum(get_factors(number)) > number:
        return 'abundant'
    #else return of aliquot sum less than number, which is called a deficient number
    return 'deficient'
        
    
        
