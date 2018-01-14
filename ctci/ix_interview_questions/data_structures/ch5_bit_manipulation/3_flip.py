import unittest
# Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0
# to a 1. Write code to find the length of the longest sequence of 1s you could 
# create.

# Ex.
# Input: 1775 (or: 1110111101111) 
# Output: 8

def flip_bit_to_win(n):
    
    prev_run = 0 
    curr_run = 0 
    curr_max = 1

    while n:
        curr_bit = n & 1
        n = n >> 1 

        if curr_bit == 1:
            curr_run += 1
        else:
            prev_run = curr_run
            curr_run = 0

        # check to update curr_max after each bit
        curr_max = max(curr_max, prev_run+curr_run+1)
        
    return curr_max

# 911 (1110001111) => 5
# 243 (11110011) => 5
# 1781 (11011110101) => 7


class Tests(unittest.TestCase):
    def test_flip(self):
        self.assertEqual(flip_bit_to_win(1775), 8)
        self.assertEqual(flip_bit_to_win(911), 5)
        self.assertEqual(flip_bit_to_win(243), 5)
        self.assertEqual(flip_bit_to_win(1781), 7)


if __name__ == '__main__':
    unittest.main()

