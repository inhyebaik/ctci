# O(N)
# Space: O(N^2) 
def string_rotation(s1, s2):
    for i in range(1, len(s1)):
        substring1 = s1[:i] # string slicing is O(N^2)
        substring2 = s1[i:]
        if substring2 + substring1 == s2:
            return True
    return False

# O(N)
def is_substring(string, substring):
    return substring in string

# O(N)
# Space: O(N)
def string_rotation2(s1, s2):
    if len(s1) == len(s2):
        return is_substring(s1+s1, s2) # string concatentation is O(N)
    return False