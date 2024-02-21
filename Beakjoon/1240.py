n,m = map(int,input().split())

graph = [[] for i in range(n+1)]
for _ in range(n-1):
    x,y,cost = map(int,input().split())
    graph[x].append([y,cost])
    graph[y].append([x,cost])
def dfs(x,dist):
    if visited[x]:
        return
    visited[x] = True
    distance[x] = dist
    for y,cost in graph[x]:
        dfs(y,dist+cost)
for i in range(m):
    x,y = map(int,input().split())
    visited = [False] * (n+1)
    distance = [-1 for i in range(n+1)]
    dfs(x,0)
    print(distance[y])