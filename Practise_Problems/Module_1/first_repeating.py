def first_non_repeating_char(s):
    hash_table = [None] * 26
    for ch_idx in range(len(s)):
        # given all characters are lower case alphabets
        idx = ord(s[ch_idx]) - 97
        if hash_table[idx] :
                return hash_table[idx][0]
        else:
            hash_table[idx] = (ch_idx,1)
    return -1


s = input()
print(first_non_repeating_char(s))