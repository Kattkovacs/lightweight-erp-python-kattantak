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
    two_random_letters_low = "".join(random.choice(string.ascii_lowercase) for i in range(2))
    two_random_letters_high = "".join(random.choice(string.ascii_uppercase) for i in range(2))
    two_random_numbers = "".join(random.choice(string.digits) for i in range(2))
    #two_spec_chars = "".join(random.choice("!\"#$%&'()*+, -./:<=>?@[\]^_`{|}~") for i in range(2))
    generated = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + two_random_numbers + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + "#&"
    return generated
