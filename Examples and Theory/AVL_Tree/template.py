import math


class TreeNode:
    def init(self, val):
        self.val = val
        self.height = 0
        self.cnt = self.freq = 1
        self.left = self.right = None

    def str(self):
        return str(self.val)


def getBalance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)



def height(root):
    if root is None:
        return -1
    return root.height


def RightRotate(y: TreeNode):
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    y.height = 1 + max(height(y.left), height(y.right))
    y.cnt = y.freq + count(y.right) + count(y.left)
    x.height = 1 + max(height(x.left), height(x.right))
    x.cnt = x.freq + count(x.right) + count(x.left)
    return x


def LeftRotate(x: TreeNode):
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    x.height = 1 + max(height(x.left), height(x.right))
    x.cnt = x.freq + count(x.right) + count(x.left)
    y.height = 1 + max(height(y.left), height(y.right))
    y.cnt = y.freq + count(y.right) + count(y.left)
    return y


def count(root):
    if root is None:
        return 0
    return root.cnt


def AVLInsert2(root, val):
    if root is None:
        return TreeNode(val)
    elif root.val == val:
        root.freq += 1
        root.cnt += 1
        return root
    else:
        if val > root.val:
            root.right = AVLInsert2(root.right, val)
        elif val < root.val:
            root.left = AVLInsert2(root.left, val)
        root.height = 1 + max(height(root.left), height(root.right))
        root.cnt = root.freq + count(root.right) + count(root.left)
        balance = getBalance(root)
        if balance > 1 and val < root.left.val:
            return RightRotate(root)
        if balance < -1 and val > root.right.val:
            return LeftRotate(root)
        if balance > 1 and val > root.left.val:
            root.left = LeftRotate(root.left)
            return RightRotate(root)
        if balance < -1 and val < root.right.val:
            root.right = RightRotate(root.right)
            return LeftRotate(root)
    return root


def search(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    elif root.val < val:
        return search(root.right, val)
    else:
        return search(root.left, val)


def inorder(root):
    if root:
        inorder(root.left)
        print(root, end = " ")
        inorder(root.right)


def AVLInsert(root, val,  i):
    global ans
    temp = rank(root, math.floor(val/2.00000001))
    ans += i - (temp - 1)
    root = AVLInsert2(root, val)
    return root


def rank(node, x):
    r = 1
    while node:
        if node.val == x:
            r += count(node.right)
            return r
        elif node.val < x:
            node = node.right
        else:
            r += node.freq + count(node.right)
            node = node.left
    return r


n = int(input())
arr = list(map(int, input().split()))
root = None
ans = 0
for i in range(n-1, -1, -1):
    root = AVLInsert(root, arr[i], i)
print(ans)
