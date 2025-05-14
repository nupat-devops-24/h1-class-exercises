"""This module converts weights from kilogramms to pounds"""


def weight_converter(user_weight):
    """Return weight in pounds given a kilogram input"""

    try:
        weight_lbs = float(user_weight) / 0.45
        return weight_lbs
    except ValueError:
        print('that was not a valid number')


def weight_converter_v2():
    """Return weight in pounds given a kilogram input"""

    try:
        weight_lbs = float(input("Enter your weight in kg: ")) / 0.45
        return weight_lbs
    except ValueError:
        print('that was not a valid number')
