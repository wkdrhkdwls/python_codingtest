N, M = map(int, input().split())

graph = []
cnt = 0
for i in range(N):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


for a in range(N):
    for b in range(M):
        if dfs(a, b) == True:
            cnt += 1

print(cnt)
