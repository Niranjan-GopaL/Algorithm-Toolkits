def DP(n):
    if n <= 2:
        return n-1
    a = 0
    b = 1
    for _ in range(n-2):
        c = (a + b) % 10
        a = b
        b = c
    return c

# For n = 1000000 (6 zeros), it gave answer really quickly
# For n = 1000000000 (9 zeros) , it didn't give answer even after 1 min!!
n_ = int(input())
print(DP(n_))