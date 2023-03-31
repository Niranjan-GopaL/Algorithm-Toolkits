# repetation in a seq
#  THIS IS NEW AND AWESOME

s = input()
ans,c = 1,0
l = 'A' 
for i in s:
    if i == l:
        c += 1
        ans = max(c,ans)
    else:
        l = i
        c = 1
print(ans)