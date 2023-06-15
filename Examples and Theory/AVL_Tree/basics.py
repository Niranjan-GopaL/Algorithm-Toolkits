'''
so suppose this :- 

    Z                      Z                     Z               Z
   /                      /                       \                 \                
  Y                      Y                         Y                 Y
 /                        \                       /                   \
X                          X                     X                     X

These are the 4 rotations that an AVL tree can go thorugh

'''


class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None

def identify_tree_type(root):
    s =''
    current = root

    while current:
        if  current.r:
            s += '1'
            current = current.r
        elif current.l:
            s += '0'
            current = current.l
        else:
            break
    return s


# Create the three trees
tree1 = Node("Z")
tree1.l = Node("Y")
tree1.l.l = Node("X")

tree2 = Node("Z")
tree2.l = Node("Y")
tree2.l.r = Node("X")

tree3 = Node("Z")
tree3.r = Node("Y")
tree3.r.r = Node("X")

# Test the identification of tree types
print(identify_tree_type(tree1))  # Output: 0
print(identify_tree_type(tree2))  # Output: 1
print(identify_tree_type(tree3))  # Output: 2