from collections import deque

k = int(input())
m, n = map(int, input().split())

graph=[list(map(int,input().split()))for _ in range(n)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]
hdx = [-2,-2,-1,-1,1,1,2,2]
hdy = [-1,1,-2,2,-2,2,-1,1]

def bfs(k):
    queue = deque()
    queue.append((0, 0, k))
    visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
    while queue:
        x, y, cnt = queue.popleft()
        if x == (n - 1) and y == (m - 1):
            return visited[x][y][cnt]
        if cnt > 0:
            for i in range(8):
                nx, ny = x + hdx[i], y + hdy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visited[nx][ny][cnt-1] == 0:
                    queue.append((nx,ny,cnt-1))
                    visited[nx][ny][cnt-1] = visited[x][y][cnt] + 1
        for j in range(4):
            nx,ny = x + dx[j], y + dy[j]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                queue.append((nx, ny, cnt))
                visited[nx][ny][cnt] = visited[x][y][cnt] + 1
    return -1

print(bfs(k))