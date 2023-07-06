from collections import deque 


def is_valid(i,j):
    print(f' i : {i} and j : {j} are valid ? : {i>=1 and i<=8 and j>=1 and j<=8} \n')
    if (1<=i and i<=8) and (1<=j and j<=8): 
        return True
    else:
        return False

def solve():
    dir_ = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),(1, -2), (1, 2), (2, -1), (2, 1)]

    depth = 0
    q = deque([(si,sj,depth)])

    while q:
        print("\n---------Queue iteration--------------")
        x = q.popleft()

        print(f' x : {x}')

        print(f' i : {x[0]} j : {x[1]} and the current depth is : {x[2]}\n')
        if (x[0],x[1]) == (ti,tj) :
            return x[2]


        for di,dj in dir_:
            i,j = x[0]+di, x[1]+dj 
            
            print(f'is the i+{di} : {i} and the j+{dj} : {j} valid ? : {is_valid(i,j)}')
            if is_valid(i,j) and not vis[i][j]:
                vis[i][j] = 1
                q.append((i,j,x[2]+1))
            print(f'queue : {q}')
            print("--------------------------------------\n")

'''

1,1     1,2     1,3     1,4     1,5     1,6     1,7     1,8

2,1     2,2     2,3     2,4     2,5     2,6     2,7     2,8

3,1     3,2     3,3     3,4     3,5     3,6     3,7     3,8

4,1     4,2     4,3     4,4     4,5     4,6     4,7     4,8

5,1     5,2     5,3     5,4     5,5     5,6     5,7     5,8

6,1     6,2     6,3     6,4     6,5     6,6     6,7     6,8

7,1     7,2     7,3     7,4     7,5     7,6     7,7     7,8

8,1     8,2     8,3     8,4     8,5     8,6     8,7     8,8


'''


vis=[[0 for i in range(9)] for j in range(9)]
print(vis)

si,sj = [6, 6]
ti,tj = [1, 1]

print(solve())