carNum = int(input())
entranceList = [input() for _ in range(carNum)]
exitList = [input() for _ in range(carNum)]
count = 0
target = carNum - 1

while entranceList != exitList:
    if entranceList[target] != exitList[target]:
        car = entranceList[target]
        exitList.remove(car)
        exitList.insert(target, car)
        count += 1
    target -= 1
print(count)