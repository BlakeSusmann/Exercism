""" Functions for validating and defining different types of triangles"""

def is_valid(sides):
    """Calculate if input sides can be a triangle 
    param sides - a, b, c in int 
    return - boolean true or false of 'is_valid' triangle

    Function checks to make sure all sides are a positive number and ensure 
    no two sides added together is less than the thrid side 'degenerative triangles'
    """
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b < c or b + c < a or a + c < b:
        return False
    return True

def equilateral(sides):
    """Calculates if 3 input sides or a triangle define the parameters 
    needed to be an equalateral triangle

    param sides - a, b, c in int
    return - boolean equilateral is True or False

    Function that takes all three sides of a triangle and checks if all three
    are equal to one aonther creating a equalateral triangle
    """
    if not is_valid(sides):
        return False
    a, b, c = sides
    if a == b and a == c:
        return True
    return False

def isosceles(sides):
    """Determine if a triangle is 'also' (because in some cases equalatieral triagnles 
    are still conisdered isosceles triangles as well) or 'is' an isoscles triangle

    param sides - a, b, c in int
    return - boolean isosceles is True or False

    Functions checks for the only requirements outside is valid triangle 
    if 2 sides (AT LEAST) are equal
    """
    a, b, c = sides
    if not is_valid(sides):
        return False
    if a == b or a == c or b ==c:
        return True
    return False
    
def scalene(sides):
    """Determine if a triangle is scalene and valid (where no sides of 
    the triangle are equal one another)

    param sides - a, b, c in int
    return - boolean scalene is True or False

    Function checks all three sides for non-equlity in values whist still determining if 
    valid triangle
    """
    a, b, c = sides
    if not is_valid(sides):
        return False
    if a != b and a != c and b != c:
        return True
    return False