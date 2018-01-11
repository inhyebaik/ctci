def one_away(s1, s2):
    """ Check if s1 can be converted to s2 with a single edit."""
    if len(s1) == len(s2):
        return one_away_replace(s1, s2)
    elif len(s1)+1 == len(s2):
        return one_away_insert(s1, s2)
    elif len(s1)-1 == len(s2):
        return one_away_insert(s2, s1)
    else:
        return False

def one_away_insert(s1, s2):
    """ Check if s1 (shorter str) is the same as s2 except for one letter. """
    i, j = 0, 0
    edited = False
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            if not edited:
                edited = True
                j += 1
            else:
                return False
    return True


def one_away_replace(s1, s2):
    """ Check if strings (of same length) are same except for one letter. """
    diff_found = False
    for a, b in zip(s1, s2):
        if a != b:
            if not diff_found:
                diff_found = True
            else:
                return False
    return True
