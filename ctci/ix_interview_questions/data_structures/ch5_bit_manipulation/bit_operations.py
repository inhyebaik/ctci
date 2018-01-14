def get_bit(num, i):
    """ Checks if ith bit is set (is 1) """
    mask = 1 << i
    return (num & mask) != 0

def set_bit(num, i):
    """ Sets ith bit to 1. """
    mask = 1 << i
    return (num | mask)

def clear_bit(num, i):
    """ Clears ith bit to 0. """
    mask = ~(1 << i)
    return num & mask

def clear_bits_MSB_to_i(num, i):
    """ Clears most significant bit to ith bit, inclusive. """
    # make a sequence of 0s followed by i 1s
    # clearing MSB is 
    mask = (1 << i)-1
    return num & mask

def clear_bits_i_to_0(num, i):
    """ Clears ith to 0th bits, inclusive. """
    # make a sequence of 1s followed by i 0s 
    mask = -1 << (i + 1)
    return num & mask
