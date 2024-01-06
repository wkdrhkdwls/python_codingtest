N, L = map(int, input().split())
# N = 물 새는 곳의 갯수
# L = 테이프 길이
T = list(map(int, input().split()))
T.sort()
cnt = 1

# print(T)
for i in T[1:]:
    if i in range(T[0], T[0] + L):
        continue
    else:
        T[0] = i
        cnt += 1

print(cnt)
