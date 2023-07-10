def solve():
    D = [1]*n
    
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]>arr[i] and D[j]<D[i]+1:
                D[j] = D[i]+1

    m = 0
    for i in range(n):
        if D[i] > D[m]:
            m = i

    return D[m]

'''TEST CASE
10
4 8 12 18 11 1 9 7 16 17
'''



n = int(input())
arr = list(map(int, input().split()))
print(solve())