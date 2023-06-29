# an extremely powerful code
# demonstrates how easy it is to 
# convert ideas into code in python


'''
dfs function that returns 1 if the grid can be
converted to a 1-bit flip and disconnect, 0 otherwise.

we traverse from 0,0 to n-1,m-1 and we'll 
flip all the 1s to 0s along the path
if even after that there exists a complete path ONLY THEN
would it be impossible to disconnect the grid.
'''
def dfs(i,j):

    if (i,j) == (len(grid)-1,len(grid[0])-1) :  return 1
    
    if not(0<=i<len(grid)) or  not(0<=j<len(grid[0])) or grid[i][j] == 0: 
        return 0

    grid[i][j] = 0 

    # any() returns true if any of the elements in the iterable are 
    # true, otherwise false similarly all() would have
    #  returned true if all the elements were true
    return any( dfs(i+di,j+dj) for di,dj in [(1,0),(0,1)] )




n = int(input())
_ = input()
grid = [list(map(int,input().split())) for _ in range(n)]


# doing dfs for the first time and setting all the 1s in the path as 0s
dfs(0,0)

grid[0][0] = 1

# doing dfs for the second time and checking if it is 
# possible to reach last bit.
# if we did reach the last bit. then dfs() returned 
# true but for us it means we can't disconnect it.
print(not dfs(0,0))