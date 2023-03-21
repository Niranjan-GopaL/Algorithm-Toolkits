def first_non_repeating_char(s):
    flag = 0
    for i_idx, i in enumerate(s[:-1]):
        for j_idx,j in enumerate(s[i_idx+1:]):
            if i == j: 
                flag = 0
                break
            elif j_idx == len(s) - 1:
                flag =1
        if flag == 1:
            return i_idx
    return -1


s = input()
print(first_non_repeating_char(s))


