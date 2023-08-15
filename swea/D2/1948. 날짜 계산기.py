T = int(input())
accum_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

for tc in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    result = accum_month[m2-1] - accum_month[m1-1] + d2 - d1 + 1
    print(f"#{tc} {result}")
