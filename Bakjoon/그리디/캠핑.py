# 브론즈1

i = 1
while True:

    L, P, V = map(int, input().split())

    if L + P + V == 0:
        break
    answer = (L * (V // P))
    answer += min((V % P), L)
    print(f"Case {i}: {answer}")

    i += 1
