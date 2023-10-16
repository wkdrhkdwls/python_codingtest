T = int(input())

array = []

for _ in range(T):
    array.append(int(input()))

array.sort(reverse=True)

# for i in range(T):
#     print(array[i], end=" ")

for i in array:
    print(i, end=" ")
