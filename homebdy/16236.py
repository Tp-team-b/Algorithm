from collections import deque

N = int(input())
state = []
x, y = -1, -1
size = 2
eat = 0  

for i in range(N):
    state.append(list(map(int, input().split())))
    for j in range(N):
        if state[i][j] == 9:
            x = i
            y = j
            state[x][y] = 0
            
def bfs(s_x, s_y, size):
    queue = deque()
    visited = [[0]*N for _ in range(N)]
    queue.append((s_x, s_y, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[s_x][s_y] = 1
    fish = []

    while queue:
        x, y, count = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if state[nx][ny] != 0 and state[nx][ny] < size:
                    fish.append((count+1, nx, ny))
                    queue.append((nx, ny, count+1))
                elif state[nx][ny] == 0 or state[nx][ny] == size:
                    queue.append((nx, ny, count+1))

    fish.sort()
    if fish:
        return [fish[0][1], fish[0][2], fish[0][0]]
    return []

result = 0

while True:
    move = bfs(x, y, size)
    if move:
        m_x, m_y, time = move
        state[x][y] = 0
        eat += 1
        result += time
        if eat == size:
            size += 1
            eat = 0
        x, y = m_x, m_y
    else:
        break

print(result)