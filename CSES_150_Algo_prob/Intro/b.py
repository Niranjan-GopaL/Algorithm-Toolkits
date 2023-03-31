# To find missing number

n = int(input())
l = map(int , input().split(' '))
s = 0
for i in l:
    s += i
print(int((n*n+n)/2 - s))