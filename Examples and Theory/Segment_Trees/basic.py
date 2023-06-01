'''
Seg trees are used when we want "range queries" in "log time"

-> Think from leaves. [[1st main point]]
   that will be the base case
-> those 3 CONDITIONS are KEYYYY
'''

from math import inf


def build(idx, l, r):
    '''Building Segment tree'''

    # base case
    if l == r : 
        segment_tree[idx] = l
        return
    # normal case
    mid = (l+r)//2
    build(2*idx + 1, l , mid)
    build(2*idx + 2, mid+1, r)

    # How you want to build the segment tree [RMQ, RSQ], you can do it below  -----\/
    # RMQ
    if inp[segment_tree[2*idx+1]] < inp[segment_tree[2*idx+2]]:
        segment_tree[idx]= segment_tree[2*idx+1]
    else:
        segment_tree[idx]= segment_tree[2*idx+2]

    '''
    Constructs the same tree that sir gave [ look at ST and BIT pptx in Course materials folder in the repo ]
    '''




inp = [24,3,45,12,7,36,73,87]
segment_tree = [-inf]*(4*len(inp))
build(0,0,len(inp)-1)
print(segment_tree)



# q = int(input())
# ans = []
# for _ in range(q):
#     l,r =list(map(int, input().split()))
#     # ans.append()

