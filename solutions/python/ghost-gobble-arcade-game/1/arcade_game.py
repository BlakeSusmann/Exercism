"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?

    Function returns true (to eat a ghost) only if power_pelletf_active and touching_ghost are
    true derived from the and boolean expersion of 'and'.
    """

    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?

    Function returns true (for Pac-Man scoring a point) if either 'touching_power_pellet' or 
    'touching_dot' is true player 'score' is then true.
    """

    return touching_power_pellet or touching_dot

def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power
    pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?

    Function returns true (GAME OVER) if Pac Man is touching and ghost and the power pellet is 
    'NOT' active (or NOT TRUE = False).
    """

    return not power_pellet_active and touching_ghost

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?

    Function returns true (Pac Man Wins!) derived from if Pac Man has eaten all the dots (True) 
    and is either not touching_ghost (True) 'or' is touching a ghost with a active
    'power_pellet_active' (True)
    """

    return has_eaten_all_dots and (power_pellet_active or not touching_ghost)
