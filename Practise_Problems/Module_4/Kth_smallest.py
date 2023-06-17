class Node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None

def build(arr,i,n):
    if i>=n :return None

    root = Node(arr[i])
    root.l = build(arr,2*i+1)
    root.r = build(arr,2*i+2)

    return root

def kthSmallest_inO1(root, k):
    n=0
    stack=[]
    cur=root
    while cur or stack :
        while cur :
            stack.append(cur)
            cur=cur.l
        cur=stack.pop()
        n +=1
        if n==k :
            return cur.val
        cur = cur.r


arr = []
def lnr(root, k):
    if root:
        lnr(root.l, k)

        if k:
            arr.append(root.val)
            k -= 1
        else:
            return

        lnr(root.r, k)


l = input().split()
k = int(input())
l = [int(i) for i in l if i != 'null']
root = build(l,0,len(l))

lnr(root, k)
print(arr[k-1]) # this is kth smallest element

# print(kthSmallest_inO1(root, k))