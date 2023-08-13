T = int(input())

for tc in range(1, T + 1):
    test = str(input())

    count = 0
    for i in range(len(test)//2):
        if test[i] == test[-1 - i]:
            count = 1
        else:
            count = 0
    print(f"#{tc} {count}")