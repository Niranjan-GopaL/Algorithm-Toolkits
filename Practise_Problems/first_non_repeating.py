def first_non_repeating_char(s):
    hash_table = [None] * 26
    for ch_idx in range(len(s)):
        # given all characters are lower case alphabets
        idx = ord(s[ch_idx]) - 97
        # first time a char is found , in hash table its maped as 1
        # but if the same char is again found then it is made to be 2
        if hash_table[idx] :
            hash_table[idx] = 2
        else:
            hash_table[idx] = 1

    # print(hash_table)
    # print()

    for ch_idx in range(len(s)):
        idx = ord(s[ch_idx]) - 97  
        if hash_table[idx] == 1:
            return ch_idx
    return -1

        
        

s = input()
print(first_non_repeating_char(s))