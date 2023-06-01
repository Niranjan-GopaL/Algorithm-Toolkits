


def build(idx, l, r):
    '''Building Segment tree'''

    # base case
    if l == r : 
        segments[idx] = inp[l]
        return
    # normal case
    mid = (l+r)//2
    build(2*idx + 1, l , mid)
    build(2*idx + 2, mid+1, r)

    # How you want to build the segment tree [RMQ, RSQ], you can do it below
    # RMaxQ
    segments[idx] = max(segments[2*idx+1], segments[2*idx+2])



inp = []
segments = []


