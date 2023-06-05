'''
    This code can do RMQ , RSQ, RMaxQ etc by modifying one part of the code


Seg trees are used when we want "range queries" in "log time"

-> Think from leaves. [[1st main point]]
   that will be the base case
-> those 3 CONDITIONS are KEYYYY
'''

from math import inf

def build(idx, ss, se):
    '''Building Segment tree'''

    # base case
    if ss == se : 
        segment_tree[idx] = inp[ss]
        return
    # normal case
    mid = (ss+se)//2
    build(2*idx + 1, ss , mid)
    build(2*idx + 2, mid+1, se)

    # How you want to build the segment tree [RMQ, RSQ], you can do it below  -----\/
    # RMQ

    #Constructs the same tree that sir gave [ look at ST and BIT pptx in Course materials folder in the repo ]
    # if inp[segment_tree[2*idx+1]] < inp[segment_tree[2*idx+2]]:
    #     segment_tree[idx]= segment_tree[2*idx+1]
    # else:
    #     segment_tree[idx]= segment_tree[2*idx+2]

    # much more easier to store the element instead of the index
    segment_tree[idx] = min(segment_tree[2*idx+1], segment_tree[2*idx+2])




def query_and_find(idx,qs,qe,ss,se):

    # if segtree's interval is COMPLETELY inside given [qs,qe]
    if ss>=qs and se<=qe:
        print(segment_tree[idx])
        return segment_tree[idx]

    elif se<qs or ss>qe: 
        return inf
    
    else:
        mid = (ss+se)//2
        left_ans = query_and_find(2*idx+1,qs,qe,ss,mid)
        right_ans = query_and_find(2*idx+1,qs,qe,ss,mid) 

        print(left_ans)
        print(right_ans)

        return min(left_ans, right_ans)


    # # if either side returns inf, we can just return the other side
    # if left_ans == inf or right_ans == inf:
    #     if left_ans < right_ans:
    #         return left_ans 
    #     else:
    #         return right_ans
    # # if niether side returns inf, and both are proper indexes from seg_tree
    # # then we compare which element in THAT IDX is least in inp array and return accordingly
    # else:
    #     if inp[left_ans] < inp[right_ans]:
    #         return left_ans
    #     else:
    #         return right_ans
         

inp = [24,3,45,12,7,36,73,87]
segment_tree = [inf]*(4*len(inp))
build(0,0,len(inp)-1)
print(segment_tree)


q = int(input())
ans = []
for _ in range(q):
    a,b =list(map(int, input().split()))
    ans.append(query_and_find(0,a,b,0,len(inp)-1))

for i in ans:
    print(i)