P, K = map(int, input().split())

if P > K:
    print(P - K + 1)
elif P == K:
    print(0)
else:
    print(P + 1000 - K)
