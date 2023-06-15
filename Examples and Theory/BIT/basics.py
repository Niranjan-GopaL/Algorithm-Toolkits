class FenwickTree:
    def __init__(self, n):
        self.n = n
        # query from i + 1 will get first i's sum
        self.bits = [0 for _ in range(self.n + 1)]
    
    def update(self, index):
        i = index + 1
        while i <= self.n:
            self.bits[i] += 1
            i += (i & -i)
    
    def query(self, index):
        i = index
        res = 0
        while i:
            res += self.bits[i]
            i -= (i & -i)
        return res
        

def reversePairs(nums):
    double_nums = [2 * num for num in nums]
    _mapping = {val:ind for ind, val in enumerate(sorted(set(double_nums + nums)))}
    ranks = [_mapping[n] for n in nums]
    double_ranks = [_mapping[n] for n in double_nums]
    
    tree = FenwickTree(2 * len(nums))
    res = 0
    for i in range(len(ranks) - 1, -1, -1):
        res += tree.query(ranks[i])
        tree.update(double_ranks[i])
    return res

