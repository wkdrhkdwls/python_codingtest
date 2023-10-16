T = int(input())

array = []

for i in range(T):
    input_data = input().split()
    name = input_data[0]
    score = input_data[1]
    array.append((name, int(score)))

array = sorted(array, key=lambda x: x[1])

for i in array:
    print(i[0], end=" ")
