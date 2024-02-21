n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
count = 0

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
print(graph)
def dfs(x):
    visited[x] = True
    global count
    count+=1
    for y in graph[x]:
        if not visited[y]:
            dfs(y)
dfs(1)
print(count-1)