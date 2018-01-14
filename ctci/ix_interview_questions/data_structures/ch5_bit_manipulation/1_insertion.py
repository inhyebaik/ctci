import unittest

# You are given two 32-bit numbers, Nand M, andtwo bit positions, land j. Write
# a method to insert M into Nsuch that M starts at bit j and ends at bit i. You
# can assume that the bits j through i have enough space to fit all of M. That is,
# if M = 10011, you canassumethat there areat least 5 bits between j and i. You
# would not,forexample, have j = 3 and i = 2,because M could notfully fit between
# bit 3 and bit 2.

def insert(n, m, i, j):

    # make mask to clear n from bits j to i 
    left_mask = (1 << j)-1
    right_mask = -1 << (i + 1)
    mask = left_mask | right_mask

    # clear n with mask; set with m, shifted in place to i 
    result = (n & mask) | (m << i)

    print bin(result)
    return result


class Tests(unittest.TestCase):
    def test_insert(self):
        f = insert(1024, 19, 2, 6)
        answer = 1100
        self.assertEqual(f, answer)
        
insert(1024, 19, 2, 6) # 0b10001001100

if __name__ == '__main__':
    unittest.main()