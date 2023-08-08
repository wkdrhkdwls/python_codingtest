T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    number = [0] * 10
    i = 1
    while 0 in number:
        res = str(N * i)
        for j in range(len(res)):
            number[int(res[j])] += 1
        i += 1

    print(f"#{tc} {res}")