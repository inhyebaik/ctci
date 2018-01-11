def string_rotation(s1, s2):
    for i in range(1, len(s1)):
        substring1 = s1[:i]
        substring2 = s1[i:]
        if substring2 + substring1 == s2:
            return True
    return False

def is_substring(string, substring):
    return substring in string
