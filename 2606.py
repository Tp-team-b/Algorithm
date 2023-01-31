N = int(input())
C = int(input())

d = {i+1: [] for i in range(N)}

for _ in range(C):
    a, b = map(int, input().split(" "))
    d[a].append(b)
    d[b].append(a)

visited = [0]*(N+1)

ans = 0


def dfs(computer):
    global ans
    if visited[computer] == 1:
        return
    else:
        visited[computer] = 1
        ans += 1

        for c in d[computer]:
            dfs(c)


dfs(1)

print(ans-1)
