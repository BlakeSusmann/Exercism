"""Produces a reversed string

example: 'stressed' returns 'desserts'
"""

def reverse(text):
    """Functions reverses a input text<string>

    param: str - input text string to be reversed
    return: reversed text <string>

    return uses <string>[start:stop:step] notation to list string 
    from last character in reverse 
    """
    return text[::-1]
