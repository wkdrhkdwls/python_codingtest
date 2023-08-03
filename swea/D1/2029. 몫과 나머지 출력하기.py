import math

T = int(input())

for i in range(1, T + 1):
    a, b = map(int, input().split())
    print("#{} {} {}".format(i, math.floor(a / b), a % b))
