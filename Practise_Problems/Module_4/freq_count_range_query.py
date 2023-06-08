'''             JUST THINK OF THEM AS DICTIONARIES THAT'S IT!!!!!!!!1


Fantastic code that uses := default_dict so that you can handle cases


CHAT - GPT'S REASON ON WHY DEFAULT_DICT

 "handle cases where a key is accessed but does not exist in the dictionary"

1.  When accessing a non-existent key, instead of raising a KeyError as a normal dictionary 
    would, a defaultdict will return the default value specified for that type.

2.  In the given code, the defaultdict(int) is used to create a dictionary where the default value 
    for any non-existent key is 0. 

This  updating the frequencies of elements the segment tree. If a key does not exist, the default value of 0 is returned, allowing easy and convenient 
incrementing of frequencies without explicitly checking for key existence.

In the build and merge functions, when merging the frequencies from child nodes 
into the parent node, the defaultdict(int) ensures that non-existent keys are initialized 
with a default frequency of 0. This way, we can directly increment the frequencies in a 
straightforward manner.

Using a defaultdict simplifies the code and eliminates the need for manual checks and 
initializations for non-existent keys. It provides a more concise and efficient way to 
handle the frequency updates in the segment tree implementation.

'''



from collections import defaultdict

class SegmentTree:

    # whenver an object is made, MAKE THE TREE TOO!!!
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [defaultdict(int)] * (4 * self.n)
        # this is good practise
        self.build(arr, 0, 0, self.n - 1)
        

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node][arr[start]] += 1
            return
        
        mid = (start + end) // 2
        
        self.build(arr, 2 * node + 1, start, mid)
        self.build(arr, 2 * node + 2, mid + 1, end)
        
        self.merge(node)
    

    def merge(self, node):
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        # THIS IS EXACTLY WHERE default_dic SHINES!!!!!!!!!
        for key in self.tree[left_child]:
            self.tree[node][key] += self.tree[left_child][key]
            
        for key in self.tree[right_child]:
            self.tree[node][key] += self.tree[right_child][key]
    
    
    def query(self, node, ss, se, qs, qe):
        
        if qs <= ss and qe >= se:
            return self.tree[node]

        if ss > qe or se < qs:
            return defaultdict(int)
        
        mid = (ss + se) // 2
        
        left_result = self.query(2 * node + 1, ss, mid, qs, qe)
        right_result = self.query(2 * node + 2, mid + 1, se, qs, qe)
        
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

