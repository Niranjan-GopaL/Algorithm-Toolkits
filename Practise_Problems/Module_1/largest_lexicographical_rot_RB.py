d = 26
q = 100_001

def find_h(M):
    h = 1
    for i in range(M-1):
        h = (h*d) % q
    return h
    

def compute_hash(s):
    p = 0
    for i in range(len(s)):
        p = (d*p + ord(s[i])) % q
    return p


def largest_lex_rotation(s):
    h = find_h(len(s))
    s = s + s
    # computing hash of first window
    first_window_hash = compute_hash(s[:len(s) // 2])
    max_hash = rolling_hash = first_window_hash

    max_idx = 0
    # creating a slide window and finding rolling hashvalues
    for i in range(len(s)//2 - 1):
        rolling_hash = (d*(rolling_hash - ord(s[i])*h) + ord(s[i+len(s) // 2])) % q
        if rolling_hash < 0:
            rolling_hash = rolling_hash + q
        if rolling_hash > max_hash:
            max_hash = rolling_hash
            max_idx = i

    return s[max_idx : len(s)//2 - max_idx]


# Example usage:
string = input()
print(largest_lex_rotation(string))
