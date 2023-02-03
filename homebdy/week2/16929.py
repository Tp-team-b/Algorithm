n, m = map(int, input().split())

graph=[list(map(str,input()))for _ in range(n)]
visited = [[0]*m for _ in range(n)]
cycle = False
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, count, start_x, start_y, color):
    global cycle
    if cycle == True:
            return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=n or nx<0 or ny>=m or ny<0:
            continue
        if start_x == nx and start_y == ny and count >= 4:
            cycle = True
            return
        if  visited[nx][ny] == 0 and graph[nx][ny] == color:
            visited[nx][ny] = 1
            dfs(nx, ny, count+1, start_x, start_y, color)
            visited[nx][ny] = 0
    return 

for i in range(n):
    if cycle == True:
        break
    for j in range(m):
        if j > 0 and graph[i][j] == graph[i][j-1]:
            continue
        visited[i][j] = 1
        dfs(i, j, 1, i, j, graph[i][j])

if cycle == True:
    print("Yes")
else:
    print("No")