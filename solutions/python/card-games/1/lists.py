"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    two_more_rounds_table = []
    
    for more_rounds_count in range(3):
        two_more_rounds_table.append(number)
        number += 1

    # this works too two_more_rounds_table = [number, (number+1), (number+2)]
    
    return two_more_rounds_table
    

    
def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    
    joined_rounds_list = rounds_1 + rounds_2
    
    return joined_rounds_list
    


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
        
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    # average of card hand sum of the value of cards 
    # divided by the number of cards in hand
    # the length of hand<list> 
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    
    first_last_card_average = hand[0]
    
    if len(hand) >= 2:
        first_last_card_average = (hand[0] + hand[-1]) / 2
        
    if first_last_card_average == card_average(hand):
        return True
        
    if len(hand) // 2 != 0:
        mid_card_position = len(hand) // 2
        if hand[mid_card_position] == card_average(hand):
            return True

            
    return False 


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_cards_table = hand[1::2]
    odd_cards_table = hand[::2]
    even_cards_average = sum(even_cards_table) / len(even_cards_table)
    odd_cards_average = sum(odd_cards_table) / len(odd_cards_table)

    if even_cards_average == odd_cards_average:
        return True
        
    return False 


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
    return hand 
