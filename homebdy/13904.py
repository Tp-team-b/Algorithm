n = int(input())
work = []
result = 0

for i in range(n):
    work.append(list(map(int, input().split())))
work.sort()

can = []
date = work[-1][0]

while date > 0:
    while work and work[-1][0] >= date:
        can.append(work.pop()[1])
    date -= 1
    if not can:
        continue
    can.sort()
    result += can.pop()

print(result)