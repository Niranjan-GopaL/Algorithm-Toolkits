'''
    This code can do RMQ , RSQ, RMaxQ etc by modifying one part of the code


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

    #Constructs the same tree that sir gave [ look at ST and BIT pptx in Course materials folder in the repo ]

def query_and_find(idx,a,b,l,r):

    # if segtree's interval is COMPLETELY inside given [a,b]
    if l>=a and r<=b:
        return segment_tree[idx]

    if r<=a or l>=b:
        return inf

    mid = (l+r)//2
    left_ans = query_and_find(2*idx+1,a,b,l,mid)
    right_ans = query_and_find(2*idx+1,a,b,l,mid)

    # if either side returns inf, we can just return the other side
    if left_ans == inf or right_ans == inf:
        if left_ans < right_ans:
            return left_ans 
        else:
            return right_ans
    # if niether side returns inf, and both are proper indexes from seg_tree
    # then we compare which element in THAT IDX is least in inp array and return accordingly
    else:
        if inp[left_ans] < inp[right_ans]:
            return left_ans
        else:
            return right_ans
         

inp = [24,3,45,12,7,36,73,87]
segment_tree = [inf]*(4*len(inp))
build(0,0,len(inp)-1)
print(segment_tree)


q = int(input())
ans = []
for _ in range(q):
    a,b =list(map(int, input().split()))
    ans.append(query_and_find(0,a,b,0,len(inp)-1))

for each_ in len(ans):
    print(each_)