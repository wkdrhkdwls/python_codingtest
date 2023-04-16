T = int(input())

for test_num in range(1, T + 1):
    data = list(map(int, input().split()))

    print("#{} {}".format(test_num, round(sum(data)/10)))
