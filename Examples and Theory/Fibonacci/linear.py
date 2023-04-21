# FUCK WHO SAID YOU CAN'T MALLOC IN PYTHON
l = [None]*(10**6)


def DP(n):
    if n <= 2:
        return n-1


    l[0] = 0
    l[1] = 1

    for i in range(2,n-2):
        l[i] = (l[i-1] + l[i-2]) % 10
    return l[i]

n_ = int(input())
print(DP(n_))