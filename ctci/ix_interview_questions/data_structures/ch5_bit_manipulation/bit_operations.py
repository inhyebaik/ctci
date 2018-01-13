def get_bit(num, i):
    """ Checks if num has an i-bit. """
    return ((num & (1 << i)) != 0)

def 