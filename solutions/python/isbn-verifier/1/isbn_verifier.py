"""Checks ISBN-10 numbers with X symbol 
check character usage

ISBN used for book identification numbers

validation equation ---> (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 
6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0 
otherwise not vaild ISBN-10
"""

def is_valid(isbn):
    """Calculate if given input string is a valid ISBN-10.

    :param isbn: string - inputted potential valid 
    ISBN will include three -,s and possible X. 
    return: bool - True if isbn total sum from mod 11 
    ISBN equation check equals 0, other wise false or throws false 
    for an incorrect character in number_digit><s>
    """

    # cleans the string of dashes and spaces
    filtered_isbn = isbn.replace('-', '').replace(' ', '')
    # checks to make check string is in 10 digit format<length>
    if len(filtered_isbn) != 10:
        return False

    # processes d1 * 10, d2 * 9... 
    isbn_total_sum = 0
    for i in range(10):
        number_digit = filtered_isbn[i]

        if i == 9 and number_digit.upper() == 'X':
            number_digit = 10
        elif number_digit.isdigit():
            number_digit = int(number_digit)
        else:
            return False

        isbn_total_sum += number_digit * (10 - i)
        
    return isbn_total_sum % 11 == 0

    

        
    
