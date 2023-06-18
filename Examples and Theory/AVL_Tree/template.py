class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    # gives the height of the node. 
    # THIS IS A VERY USEFUL wayy cuz it takes care of NULL nodes to have -1 ( here 0 ) height
    def _get_height(self, node):
        if  node is None:
            return 0
        return node.height

    # returns if its balanced or not
    def _get_balance(self, node):
        if  node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def insert(self, key):
        self.root = self._insert(self.root, key)

    # assume all unique keys 
    def _insert(self, root, key):
        if not root:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        
        # updating height of the inserted node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # checking if the Node is balanced ( difference of height of children nodes are less than a bound)
        balance = self._get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        
        if balance < -1:
            if key > root.right.key:
                return self._rotate_left(root)
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)
        
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root
        
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor = self._get_min_value_node(root.right)
                root.key = successor.key
                root.right = self._delete(root.right, successor.key)
        
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        if balance > 1:
            if self._get_balance(root.left) >= 0:
                return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        
        if balance < -1:
            if self._get_balance(root.right) <= 0:
                return self._rotate_left(root)
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)
        
        return root

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y


    def _lnr(self, node):
        if node:
            self._lnr(node.left)
            print(node.key, end=" ")
            self._lnr(node.right)

    def lnr(self):
        self._lnr(self.root)

    # Add other traversal methods (inorder, postorder) if needed


# Usage example
avl_tree = AVLTree()
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.insert(40)
avl_tree.insert(0)
avl_tree.insert(0)
avl_tree.insert(35)
avl_tree.insert(300)

avl_tree.lnr()  
print()
print()


avl_tree.delete(10)
avl_tree.lnr()  
print()