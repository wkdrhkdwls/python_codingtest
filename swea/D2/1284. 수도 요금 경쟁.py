T = int(input())
for i in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    costA = P * W
    costB = Q
    if W > R:
        costB += (W - R) * S
    print(f"#{i} {costA}") if costA < costB else print(f"#{i} {costB}")
