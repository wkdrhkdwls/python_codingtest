N = int(input())
for test in range(1, N + 1):
    data = map(int, input().split())
    answer = 0
    for i in data:
        if i % 2 == 1:
            answer += i
    print("#{} {}".format(test, answer))

