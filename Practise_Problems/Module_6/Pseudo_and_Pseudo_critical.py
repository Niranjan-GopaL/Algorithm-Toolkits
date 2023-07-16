class DSU:
    def __init__(self):
        self.parents = [i for i in range(n)]
        self.sz = [1]*n

    def find(self,x):
        if x == self.parents[x]: return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self,u,v):
        u = self.find(u); v = self.find(v)
        if u != v:
            if self.sz[u] < self.sz[v]:
                u,v = v,u
            self.parents[v] = u
            self.sz[u] += self.sz[v]


def Krushkal():
    dsu = DSU() 
    edges.sort(key=lambda e:e[3])
    print(f'\n\nEdges inside Krushkal\'s : {edges} \n\n  ')
    print(f'Before')
    print(f'parent : {dsu.parents}')
    print(f'sizes  : {dsu.sz}\n\n\n')
    
    mst_w = 0
    for i,u,v,w in edges:
        print(f'i : {i}  u : {u}  v : {v}  w : {w} ')
        print(f'find(u) : {dsu.find(u)}  dsu.find(v) : {dsu.find(v)} ')
        if dsu.find(u) != dsu.find(v):
            dsu.union(u,v)
            mst_w += w
        print(f'----- mst_w : {mst_w} <---------------------------------')
        print(f'parent : {dsu.parents}')
        print(f'sizes  : {dsu.sz}\n')
    
    print(f'\n\n\n\nAfter')
    print(f'parent : {dsu.parents}')
    print(f'sizes  : {dsu.sz}')


    return mst_w






def Find_Critical_and_Pseudo_Critical_Edges():
    MST_w = Krushkal()
    epsilon = 1
    crit , pcrit = [] , []

    for edge in edges:
        print(f'\n------ Looking at edge : {edge[0]} -----------------------------------------------------------------\n\n\n')

        print(f'crit : {crit}  pcr: {pcrit} \n\n ')

        edge[3] += epsilon 
        print(f'Edges inside solve fn : {edges} \n\n  ')
        ST_w = Krushkal()
        edge[3] -= epsilon 

        print(f'ST_w : {ST_w}  MST_w : {MST_w} ')
        if ST_w > MST_w:
            crit.append(edge[0])
        elif ST_w == MST_w:
            edge[3] -= epsilon
            MMST_w = Krushkal()        
            print("---> YAY!!!")
            print(f'MMST_w : {MMST_w}  MST_w : {MST_w} ')
            if MMST_w < MST_w:
                pcrit.append(edge[0])
            edge[3] += epsilon
        
        print(f'-----------------------------------------------\n\n')

    return f'{len(crit)} {len(pcrit)}'


''' TEST CASES
5
7
0 1 1
1 2 1
0 3 2
0 4 3
3 4 3
1 4 6
2 3 2
'''

n = 5
parent = [i for i in range(n)] 
sz = [1]*n; edges = []
edges = [[0, 0, 1, 1], [1, 1, 2, 1], [2, 0, 3, 2], [6, 2, 3, 2], [3, 0, 4, 3], [4, 3, 4, 3], [5, 1, 4, 6]]
print(f'\n\n ---------------- ORIGINAL ELDGES -------------- \n{edges} \n\n  ---------------------------')
print(Find_Critical_and_Pseudo_Critical_Edges())