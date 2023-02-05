import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())

graph = [list(map(int,input().split()))for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count = 2
result = sys.maxsize

def check_map(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = count
        for dx, dy in (0,1),(0,-1),(1,0),(-1,0):
            nx = x + dx
            ny = y + dy
            check_map(nx, ny)
        return True
        
def bfs(k):
    global result
    q = deque()
    visited = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == k:
                q.append((i,j))
                visited[i][j] = 0
    while q:
        x, y = q.popleft()
        for a,b in (0,-1),(0,1),(1,0),(-1,0):
            nx = x+a
            ny = y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > 0 and graph[nx][ny] != k:
                result = min(result, visited[x][y])
                return
            if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))


for i in range(n):
    for j in range(n):
        if check_map(i, j) == True:
            count += 1

for i in range(2, count):
    bfs(i)


print(result)