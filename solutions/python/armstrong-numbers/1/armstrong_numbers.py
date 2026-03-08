"""Function that checks whether a number is 
an Armstrong number or not 

Armstrong numbers are numbers that the 
sum of its own digits raised to the power 
of the number of digits  is the same as 
the number 

 9 = 9  ^ 1 = 9
 153 is 
 1 ^ 3 = 1 
 5 ^ 3 = 125 
 3 ^ 3 = 27   1 + 125 + 27 = 153 
"""

def is_armstrong_number(number):
    """Take a given input number 
    break number into split digits if needed and mulitiple 
    digits in container by the amount of containers (ie the 
    amount of digits in orginal input number)

    :param input: int - number containing any number (technically positive 
    for code but not valuerrors programmed or checked for this project)
    :return: bool - True or False if 'number' "is equal to sum" of 
    the digits (of the number) to power of the number of digits (in number)
    """
    
    number_string = str(number)
    expon_number = len(number_string)
    number_string.split()
    count = expon_number
    total_to_check = 0
    while count != 0:
        total_to_check += int(number_string[count - 1]) ** expon_number
        count -= 1 
    return total_to_check == number
