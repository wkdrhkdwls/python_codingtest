from collections import deque

N = int(input())
D = deque([i for i in range(1, N + 1)])

while len(D) > 1:
    D.popleft()
    move = D.popleft()
    D.append(move)

print(D[0])