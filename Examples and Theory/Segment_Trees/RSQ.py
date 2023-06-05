# The problem of RSQ can be done by
#                prefix sum methode 
#       -> Sum -- O(1)
#       -> Update ---O(n)

# given list
inp = list(map(int,input().split()))

# make a prefix sum array [ CUMULATIVE SUM before i including ai is bi ]
sum_ = 0
prefix_sum_array = []
for idx,elem in enumerate(inp):
    sum+=elem
    prefix_sum_array.append(sum)

# so if query is from l to r
# RSQ = prefix_sum_array[r] - prefix_sum_array[l]

# But update is constly, since we need to update the entire prefix array from that idx on


# Seg_tree optimises this