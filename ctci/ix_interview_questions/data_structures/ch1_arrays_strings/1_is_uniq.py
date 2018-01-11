# O(N) 

def is_uniq(string):
    # Assuming ASCII characters
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]

    for char in string:

        # get ascii number of char
        val = ord(char)
        
        if char_set[val]:
            return False
        else:
            char_set[val] = True
    
    return True


