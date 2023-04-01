def compute_lps_array(string):
    # Compute the LPS (Longest Proper Prefix-Suffix) array of the given string
    # Returns the LPS array
    n = len(string)
    lps = [0] * n
    i = 1
    length = 0
    while i < n:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def largest_lex_rotation(string):
    # Find the largest lexicographical rotation of the given string
    # Returns the starting position of the largest lexicographical rotation
    n = len(string)
    lps = compute_lps_array(string)
    pos = lps[n-1]
    while pos > 0 and lps[pos-1] == lps[n-1]:
        pos = lps[pos-1]
    if pos == 0:
        return n
    else:
        return pos

# Example usage:
string = input()
largest_rotation = largest_lex_rotation(string)
print(string[largest_rotation:] + string[:largest_rotation])
