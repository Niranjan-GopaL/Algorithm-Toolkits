def dfs(i, cnt):

    if vis[i]: return cnt

    vis[i] = 1
    cnt = 1

    for x in edges[i]:
        if not vis[x]:
            cnt +=dfs(x, cnt)

    return cnt



# n = int(input())
n = 5
vis = [0]*n
# edges = [[2],[],[],[]]

edges =[[1,4],[],[3],[],[]]

cnt = []
cmpt = 0

for i in range(n):
    if not vis[i]:
        cnt.append(dfs(i, 0))
        cmpt += 1


sm = 0
for i in range(cmpt):
    for j in range(i+1,cmpt):
        sm += cnt[i]*cnt[j]

print(sm)