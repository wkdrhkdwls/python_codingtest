T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    high = N if N > M else M
    low = M if N > M else N
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    one = 0
    two = 0
    for i in range(0, low):
        one += a[i] * b[i]
    if len(a) < len(b):
        for i in range(0, low):
            two += a[i] * b[high - low + i]
    else:
        for i in range(0, low):
            two += a[high - low + i] * b[i]

    print(f"#{tc} {one}") if one > two else print(f"#{tc} {two}")
