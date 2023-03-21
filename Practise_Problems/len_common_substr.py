_ = int(input())
l1 = list(map(int, input().split(' ')))

_ = int(input())
l2 = list(map(int, input().split(' ')))

substrings = []
substring = []
flag = 0

for p1_idx,p1 in enumerate(l1):
    temp = p1_idx
    for p2 in l2:
        if p1_idx < len(l1):
            if l1[p1_idx] != p2 :
                if flag == 1:
                    substrings.append(substring)
                    substring = []
                    flag = 0
                    p1_idx = temp
                continue
            else:
                substring.append(p2)
                p1_idx += 1
                flag = 1
print(len(max(substrings)))