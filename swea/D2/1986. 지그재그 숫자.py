N = int(input())
for i in range(N):
    T = int(input())
    res = 0
    for tc in range(1, T + 1):
        if tc % 2 != 0:
            res += tc
        else:
            res -= tc
    print(f"#{i + 1} {res}")
