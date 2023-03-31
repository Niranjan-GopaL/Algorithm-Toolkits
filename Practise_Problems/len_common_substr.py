# n = int(input())
l1 = list(map(int, input().split(' ')))

# m = int(input())
l2 = list(map(int, input().split(' ')))

substrings = []
substring = []
flag = 0

for p1_idx,p1 in enumerate(l1):
    temp = p1_idx
    for p2_idx,p2 in enumerate(l2):
        if p1_idx < len(l1):# to check if we increased p1_idx to unbounded value

            if l1[p1_idx] == p2:
                substring.append(p2)
                p1_idx  += 1
                if p2_idx == len(l2) - 1:# check the only edge case when last element is part of a common substring
                    print(substring)
                    substrings.append(substring)
                    substring = []
            else:
                if substring:
                    print(substring)
                    substrings.append(substring)
                    substring = []
                p1_idx = temp

                # handling another edge case 
                if l1[p1_idx] == p2:
                    substring.append(p2)
                    p1_idx  += 1
                continue
    
print(substrings)
print(max(map(len , substrings)))