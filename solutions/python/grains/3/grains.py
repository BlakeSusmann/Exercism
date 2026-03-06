"""Chess Grains kind paid a servant for a great duty 
the request was a chess board with grains doubling on every square 
starting on square #1 with one grain, square #2 two grains, and
square #3 with 4 grains... till 64 final square of the chess
board
"""
def square(number):
    """ Calculates the number of grains on any given square
    of the chess borad between 1 and 64 (total squares of a chess
    board)

    param number: positive integer between and including 1 and 64 
    return: int num total grains for that tile #

    Functions raises 'ValueError' for zero, negative, or numbers above 64. 
    Function take square number input and returns number of grains on that 
    specific tile 'square-number'
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")    
    if number == 1:
        return number
    return 2 ** (number - 1)
        

def total():
    """Calculates total grains for the entire chess board
    """
    grains_total = 0
    for tiles in range(1, 65):
        grains_total += square(tiles)
    return grains_total
        
        
