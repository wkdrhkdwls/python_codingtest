N = int(input())
data = list(map(int, input().split()))
data.sort()
medi = round(N//2)
print(data[medi])

