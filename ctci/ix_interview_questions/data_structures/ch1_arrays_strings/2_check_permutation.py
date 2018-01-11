from collections import Counter

def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)

