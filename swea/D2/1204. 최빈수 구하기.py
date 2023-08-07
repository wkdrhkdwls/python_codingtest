T = int(input())

for _ in range(T):
    TC = int(input())
    Score = list(map(int, input().split()))
    data = [0] * 1001

    for i in Score:
        data[i] += 1
    max_value = max(data)
    result = []
    for i in range(len(data)):
        if data[i] == max_value:
            result.append(i)
    print("#%d %d" % (TC, max(result)))
