import copy


def getHammingDistance(start, end):
    difference = []

    for i, data in enumerate(start):
        if end[i] != data:
            difference.append(i)

    return difference


def getHammingPath(start, difference):
    path = [a]
    visited = []
    difference = copy.deepcopy(difference)

    i = start
    while len(visited) != (codeCount - len(path)) and len(difference) != 0:
        if i in path or i in visited:
            i += 1
            if i >= codeCount:
                i = 0
            continue
            
        HammingDistance = getHammingDistance(codeList[path[len(path) - 1]], codeList[i])
        if len(HammingDistance) == 1 and HammingDistance[0] in difference:
            path.append(i)
            difference.remove(HammingDistance[0])
            visited.clear()

        else:
            visited.append(i)

        i += 1
        if i >= codeCount:
            i = 0

    if len(difference) == 0:
        return path
    else:
        return None


print("입력하세요.")

codeCount, codeLength = map(int, input().split())
codeList = []
pathList = []

for i in range(codeCount):
    codeList.append(input())

a, b = map(int, input().split())
a, b = a - 1, b - 1

a_b_difference = getHammingDistance(codeList[a], codeList[b])

for i in range(codeCount):
    if getHammingPath(i, a_b_difference) is not None:
        pathList.append(getHammingPath(i, a_b_difference))

if len(pathList) == 0:
    print("-1")

else:
    shortest = codeCount
    for i, path in enumerate(pathList):
        if len(path) < shortest:
            shortest = i

    for i, path in enumerate(pathList):
        for j, num in enumerate(path):
            pathList[i][j] = num + 1

    pathList[shortest] = list(map(str, pathList[shortest]))
    print(" ".join(pathList[shortest]))

