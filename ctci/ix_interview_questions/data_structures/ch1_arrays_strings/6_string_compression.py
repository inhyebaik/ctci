def compress_string(string):
    ch_counts = []
    count = 1

    for i in range(1, len(string)):
        if string[i-1] != string[i]:
            ch_counts.append(string[i-1] + str(count))
            count = 1
        else:
            count += 1

    # add last character and its count
    ch_counts.append(string[-1] + str(count))

    compressed = "".join(ch_counts) 

    return min(string, compressed, key=len)





