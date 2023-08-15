T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    num_90 = [[0 for _ in range(N)] for _ in range(N)]
    num_180 = [[0 for _ in range(N)] for _ in range(N)]
    num_270 = [[0 for _ in range(N)] for _ in range(N)]
    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            num_90[i][j] = num[N - 1 - j][i]
    for i in range(N):
        for j in range(N):
            num_180[i][j] = num_90[N - 1 - j][i]
    for i in range(N):
        for j in range(N):
            num_270[i][j] = num_180[N - 1 - j][i]

    for i in range(N):
        for j in range(N):
            print(num_90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(num_180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(num_270[i][j], end='')
        print()
