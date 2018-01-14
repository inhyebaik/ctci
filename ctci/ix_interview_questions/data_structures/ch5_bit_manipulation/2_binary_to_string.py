import unittest
# Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed 
# in as a double, print the binary representation. If the number cannot be represented 
# accurately in binary with at most 32 characters, print "ERROR:'


def dec_to_bin_string(f):
    bin_string = ["."]
    while f:
        # take ones place (1 or 0 when multiplying a float by 2) as an integer
        bit = int( (f*2) // 1 ) 

        # append the bit as a string
        bin_string.append(str(bit))

        # go to next decimal place
        f = (f * 10) % 1

    if len(bin_string) > 31:
        print "ERROR"
    else:   
        print "".join(bin_string)
        return "".join(bin_string)

class Tests(unittest.TestCase):
    def test_dec_to_bin_string(self):
        f = dec_to_bin_string(0.625)
        answer = '.101'
        self.assertEqual(f, answer)

if __name__ == '__main__':
    unittest.main()
