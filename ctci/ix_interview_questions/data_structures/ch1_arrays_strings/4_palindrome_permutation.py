from collections import Counter

def palindrome_permutation(string):
    """ 
    Check if a string is a permutation of a palindrome.
    @input: 'Tact Coa'
    @output: True (permutations: 'taco cat', 'atco cta', etc.)
    """

    table = [0 for _ in range(26)]
    odds = 0
    # remove spaces, make case-insensitive, and get alphabet index of each letter
    for c in string:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2: #if odd count
                odds += 1
            else:
                odds -= 1
    return odds <= 1

# even length strings will have at most 0 odds
# odd length strings will have at most 1 odd

def char_number(c):
    a, z = ord('a'), ord('z')
    A, Z = ord('A'), ord('Z')
    val = ord('c')

    # lowercase letter
    if a <= val <= z:
        return val - a
    # uppercase letter
    elif A <= val <= Z: 
        return val - A
    # not a letter
    else: 
        return -1




