T = int(input())

for num in range(1, T + 1):
    N = int(input())

    a_list = [2, 3, 5, 7, 11]
    arr = 5 * [0]
    for i in range(len(a_list)):
        while True:
            if N % a_list[i] == 0:
                N = N // a_list[i]
                arr[i] += 1
            else:
                break
    print(f"#{num} {' '.join(map(str, arr))}")

