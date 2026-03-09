"""Calculate a dart landing center of dart board is (0, 0)
radius to center from 10 point circle 1, 5 point circle 5
and 1 point circle 10. outside board worth 0 points
"""

def score(x, y):
    """avoiding the square root calculation
    with dist_squared equation
    """
    dist_squared = x**2 + y**2
    if dist_squared <= 1:
        return 10
    if dist_squared <= 25:
        return 5
    if dist_squared <= 100:
        return 1
    return 0








    