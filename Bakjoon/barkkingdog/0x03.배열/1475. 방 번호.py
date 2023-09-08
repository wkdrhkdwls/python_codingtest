T = input()

arr = [0] * 10

for i in T:
    arr[int(i)] += 1
    if i == '6' and arr[6] > arr[9]:
        arr[6] -= 1
        arr[9] += 1
    elif i == '9' and arr[6] < arr[9]:
        arr[6] += 1
        arr[9] -= 1
print(max(arr))
