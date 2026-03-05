"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget, exchange_rate):
    """Calculate value after exchange.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.

    Function that takes a budgeted amount of money planned for a currency exchange as an
    arguement and returns the value of the exchanged currency based on the 'exchange_rate'.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.

    Function that returns the amount of money left from (or in) the budget that is not exchanged 
    for other currency during the currency exchange.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate value of a total number of bills of a certain demonination.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.

    Function returns total cash value of a number of bills without fractions or partial bills
    to currency.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculate the number of bills (of a single denomination) into an amount.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.

    Function returns the number of (whole) currency bills that fit into the starting amount.
    """

    return int(amount / denomination)
    

def get_leftover_of_bills(amount, denomination):
    """Calculate left over dollar amount that cannot be returned from bill demonination division.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.

    Function returns the leftover (in dollars) amount that cannot be returned from your starting
    amount given the denomination of bills used for currency exchange. 
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate (in dollars) value after exchange (complete exchange process and fees).

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.

    Function that takes bill denomination payout size as an arguement and returns exchange
    (total returned) money value based on the 'budget', 'exchange_rate', and (fee) 'spread'.
    """

    exchange_fee_percentage_add = (spread / 100) * exchange_rate
    fee_adjusted_exchange_rate = exchange_rate + exchange_fee_percentage_add 
    return int((budget / fee_adjusted_exchange_rate) / denomination) * denomination
