""" Functions for validating and defining different types of triangles"""

def is_valid(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b < c or b + c < a or a + c < b:
        return False
    return True

def equilateral(sides):
    if not is_valid(sides):
        return False
    a, b, c = sides
    if a == b and a == c:
        return True
    return False

def isosceles(sides):
    a, b, c = sides
    if not is_valid(sides):
        return False
    if a == b or a == c or b ==c:
        return True
    return False
    
def scalene(sides):
    a, b, c = sides
    if not is_valid(sides):
        return False
    if a != b and a != c and b != c:
        return True
    return False