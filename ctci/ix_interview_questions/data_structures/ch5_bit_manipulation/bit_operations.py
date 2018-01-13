def get_bit(num, i):
    """ Checks if num has an i-bit. """
    return ((num & (1 << i)) != 0)

def set_bit(num, i):
    """ Sets i-bit in num to 1. """
    return (num | (1 << i))

def clear_bit(num, i):
    """ Clears i-bit in num.  """    
    mask = ~(1 << i)
    return num & mask

def clear_bits_MSB_to_i(num, i):
    """ Clears bits from most significant to i, inclusive. """
    mask = (1 << i) - 1
    return num & mask

def clear_bits_0_to_i(num, i):
    mask = -1 << (i + 1)
    return num and mask

def update_bit(num, i, value):
    """ Set ith bit to value. """
    if value == 0:
        clear_bit(num, i)
    else:
        set_bit(num, i)

def update_bit2(num, i, value):
    """ Set ith bit to value. """
    # clear ith bit with mask
    mask = ~(1 << i)
    # set ith bit with OR
    return (num & mask) | (value << i)
