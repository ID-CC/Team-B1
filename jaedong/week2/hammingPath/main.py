import copy


def getHammingDistance(start, end):
    difference = []

    for i, data in enumerate(start):
        if end[i] != data:
            difference.append(i)

    return difference


def getHammingPath(difference):
    stack = [a]
    visited = [[-1, -1]]

    while len(stack) > 0:
        flag = False
        for i in range(codeCount):
            if i in stack:
                continue

            c, d = visited[0]

            hammingDistance = getHammingDistance(codeList[stack[-1]], codeList[i])
            if len(hammingDistance) == 1 and hammingDistance[0] in difference:
                if len(stack) + 1 == c and i == d:
                    continue

                stack.append(i)
                visited = [[len(stack), i]]

                if i == b:
                    path = copy.deepcopy(stack)
                    pathList.append(path)
                    stack.pop()
                else:
                    flag = True

        if not flag:
            visited = [[len(stack), stack.pop()]]

print("입력하세요.")

codeCount, codeLength = map(int, input().split())
codeList = []
pathList = []

for i in range(codeCount):
    codeList.append(input())

a, b = map(int, input().split())
a, b = a - 1, b - 1

a_b_difference = getHammingDistance(codeList[a], codeList[b])
getHammingPath(a_b_difference)

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
