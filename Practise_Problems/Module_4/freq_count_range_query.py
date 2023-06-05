'''
Fantastic code that allows 

'''


from collections import defaultdict

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [defaultdict(int)] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
        

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node][arr[start]] += 1
            return
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        self.build(arr, left_child, start, mid)
        self.build(arr, right_child, mid + 1, end)
        
        self.merge(node)
    
    def merge(self, node):
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        for key in self.tree[left_child]:
            self.tree[node][key] += self.tree[left_child][key]
            
        for key in self.tree[right_child]:
            self.tree[node][key] += self.tree[right_child][key]
    
    def query(self, node, start, end, left, right):
        if start > right or end < left:
            return defaultdict(int)
        
        if left <= start and right >= end:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        left_result = self.query(left_child, start, mid, left, right)
        right_result = self.query(right_child, mid + 1, end, left, right)
        
        result = defaultdict(int)
        for key in left_result:
            result[key] += left_result[key]
            
        for key in right_result:
            result[key] += right_result[key]
            
        return result

# Example usage
arr = [1, 2, 1, 3, 4, 2, 1]
tree = SegmentTree(arr)

left = 1
right = 5
result = tree.query(0, 0, tree.n - 1, left, right)
for key in result:
    print(f"Element {key} appears {result[key]} times in the range [{left}, {right}]")

