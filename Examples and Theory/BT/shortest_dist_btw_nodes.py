import collections as c

class Node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None


def pathToNode(root, path, k):
 
    # base case handling
    if not root:
        return False
 
     # append the node value in path
    path.append(root.val)
  
    # See if the k is same as root's val
    if root.val == k :
        return True
  
    # Check if k is found in l or r
    # sub-tree
    if ((root.l != None and pathToNode(root.l, path, k)) or
            (root.r!= None and pathToNode(root.r, path, k))):
        return True
  
    # If not present in subtree rooted with root,
    # remove root from path and return False
    path.pop()
    return False
 


def distance(root, data1, data2):
    if root:
        # store path corresponding to node: data1
        path1 = []
        pathToNode(root, path1, data1)
 
        # store path corresponding to node: data2
        path2 = []
        pathToNode(root, path2, data2)
 
        # iterate through the paths to find the
        # common path length
        i=0
        while i<len(path1) and i<len(path2):
            # get out as soon as the path differs
            # or any path's length get exhausted
            if path1[i] != path2[i]:
                break
            i = i+1

        return (len(path1)+len(path2)-2*i)
    else:
        return 0
    
root = Node(1)
root.l = Node(2)
root.r = Node(3)
root.l.l = Node(4)
root.r.r= Node(7)
root.r.l = Node(6)
root.l.r = Node(5)
root.r.l.r = Node(8)

dist = distance(root, 4, 5)
print ("Distance between node {} & {}: {}".format(4, 5, dist))
 
dist = distance(root, 4, 6)
print ("Distance between node {} & {}: {}".format(4, 6, dist))
 
dist = distance(root, 3, 4)
print ("Distance between node {} & {}: {}".format(3, 4, dist))
 
dist = distance(root, 2, 4)
print ("Distance between node {} & {}: {}".format(2, 4, dist))
 
dist = distance(root, 8, 5)
print ("Distance between node {} & {}: {}".format(8, 5, dist))