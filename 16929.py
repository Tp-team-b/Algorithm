from sys import stdin
N, M = map(int, input().split(" "))

space = [[] for i in range(N)]
for i in range(N):
    t = stdin.readline()
    for j in range(M):
        space[i].append(t[j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
v = [[0]*M for _ in range(N)]

ans = 0


def check(x, y, start_x, start_y, step, visited):
    global ans
    if ans == 1:
        return

    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]

        if 0 <= new_x < N and 0 <= new_y < M and space[x][y] == space[new_x][new_y]:
            if new_x == start_x and new_y == start_y and step >= 3:
                ans = 1
                return
            elif visited[new_x][new_y] == 0:
                visited[new_x][new_y] = 1
                check(new_x, new_y, start_x, start_y, step+1, visited)
                visited[new_x][new_y] = 0

    # return False


for i in range(N):
    for j in range(M):
        v[i][j] = 1
        check(i, j, i, j, 0, v)
        if ans == 1:
            print("Yes")
            break
        v[i][j] = 0
    if ans == 1:
        break

if ans == 0:
    print("No")
