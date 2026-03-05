"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
   
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time (in minutes) already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time needed for the lasagna.

    :param number_of_layers: int - amount of layers chosen for lasagna build.
    :return: int - total required preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers of the lasagna as an argument and returns how many   
    minutes actual preparation time will take for the lasagna based on the 'PREPARATION_TIME'.
    """
    
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total (current) elapsed time of making lasagna.

    :param number_of_layers: int - amount of layers chosen for lasagna build.
    :param elapsed_bake_time: int - baking time (in minutes) already elapsed.
    :return: int - elapsed time in minutes (prepping + baking) derived from
    'preparation_time_in_minutes' and 'elapsed_bake_time'.

    Function that takes the actual minutes the lasagna has been in the oven and the preparation
    time taken to build the lasagna as an argument and returns (in minutes) the total elapsed 
    time of prepping and baking the lasagna currently based on the 'preparation_time_in_minutes' 
    and 'elapsed_bake_time'.
    """
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time 
