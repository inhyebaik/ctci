# Next Number: Given a positive integer, print the next smallest and the next 
# largest number that have the same number of 1 bits in their binary 
# representation.

# source: http://www.yujinc.com/5-4-next-number-cci/

def get_next_bin_same_ones(num):
    higher = higher_bin_same_ones(num)

def higher_bin_same_ones(num):
    count_ones = 0
    count_zeros = 0
    current_bit = num & 1

    while count_ones == 0 or current_bit == 1:
        if current_bit == 1:
            count_ones += 1
        else:
            count_zeros += 1
        current_bit = (num << (count_zeros+count_ones) & 1)

    # position of where the next 1 will be 
    pos = count_ones + count_zeros
    # get next largest num with biggest bin (trailing 0s) w/ the rest of num's bins 
    flipped = (1 << pos) ^ num
    # clear the smallest positions up to where we will add remaining 1s
    clear_smallest = flipped & (~0 << pos)
    # make mask with ones... -1 for the highest position already taken
    mask = (1 << (count_ones-1)) - 1
    return clear_smallest | mask
    

    