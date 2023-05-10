arr = list(map(int , input().split()))
arr.sort()

s = set()

for i in range(0, len(arr)-1):

    l = i + 1
    r = len(arr) - 1
    x = arr[i]
    while (l < r):

        if (x + arr[l] + arr[r] == 0):
            s.add((x, arr[l], arr[r]))
            l += 1
            r -= 1

        elif (x + arr[l] + arr[r] < 0):
            l += 1

        else:
            r -= 1

print(s)