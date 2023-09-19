from collections import deque

N, M = map(int, input().split())
selectNum = list(map(int, input().split()))
D = deque([i for i in range(1, N + 1)])

count = 0

for i in selectNum:
    while True:
        if D[0] == i:
            D.popleft()
            break
        else:
            if len(D)/2 > D.index(i):
                while D[0] != i:
                    D.append(D.popleft())
                    count += 1
            else:
                while D[0] != i:
                    D.appendleft(D.pop())
                    count += 1

print(count)
