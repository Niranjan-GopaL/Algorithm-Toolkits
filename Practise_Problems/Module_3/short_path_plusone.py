class Node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None


def pathToNode(root, path, val):
 
    if root is None:
        return False
 
    path.append(root.val)
    if root.val == val :
        return True
  
    if ((root.l  and pathToNode(root.l, path, val)) or
            (root.r and pathToNode(root.r, path, val))):
        return True
    path.pop()
    return False
 


 
def distance(root, data1, data2):
        path1 = []
        pathToNode(root, path1, data1)
        # now path1 will have path to node of data1 
 
        path2 = []
        pathToNode(root, path2, data2)
        # now path2 will have path to node of data2 
 
        i=0
        while i<len(path1) and i<len(path2):
            if path1[i] != path2[i]:
                break
            i = i+1
 
        return (len(path1)+len(path2)-2*i)


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