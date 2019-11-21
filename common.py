""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''    
    two_random_letters_low = "".join(random.choice("abcdefghijklmnopqrstvwxyz") for i in range(2))
    two_random_letters_high = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(2))
    two_random_numbers = "".join(random.choice("0123456789") for i in range(2))
    #two_spec_chars = "".join(random.choice("!\"#$%&'()*+, -./:<=>?@[\]^_`{|}~") for i in range(2))
    generated = random.choice("abcdefghijklmnopqrstvwxyz") + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + two_random_numbers + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + random.choice("abcdefghijklmnopqrstvwxyz") + "#&"
    return generated
