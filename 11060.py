N = int(input())
space = list(map(int, input().split(" ")))

dp = [N]*N
dp[0] = 0
for i in range(N):
    for j in range(1, space[i]+1):
        if i+j < N:
            dp[i+j] = min(dp[i]+1, dp[i+j])


if dp[N-1] == N:
    print(-1)
else:
    print(dp[N-1])
