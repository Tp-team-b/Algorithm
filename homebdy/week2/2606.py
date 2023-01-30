n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
result = 0

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)

def dfs(v):
    global result
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            result += 1

dfs(1)
print(result)