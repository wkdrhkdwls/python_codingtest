K = int(input())
stk = []

for i in range(K):
    T = int(input())
    if T==0:
        stk.pop()
    else:
        stk.append(T)

print(sum(stk))

# 스택개념을 잘 이해하자!