n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
result = 0
first = data[0]
second = data[1]
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    result += second
    m -= 1
    if m == 0:
        break

print(result)
