""" RainDrops Function - convert number into its corresponding
raindrop sound. 3 divisible = Pling
5 divisible= Plang 
7 divisible = Plong
"""

def convert(number):
    """ answer needs to add strings together if number is divisible 
    by 3 and 5 or 3, 5, and 7, also function returns number as a
    string if not divisible, as requested in project requirements
    """
    answer = ''
    if number % 3 == 0:
        answer += 'Pling'
    if number % 5 == 0:
        answer += 'Plang'
    if number % 7 == 0:
        answer+= 'Plong'
    if answer == '':
        return str(number)
    return answer
    