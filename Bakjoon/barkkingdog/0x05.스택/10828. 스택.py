import sys

N = int(input())

stk = []
for i in range(N):
    T = sys.stdin.readline().split()

    if T[0] == "push":
        stk.append(T[1])
    elif T[0] == "pop":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif T[0] == "size":
        print(len(stk))
    elif T[0] == "empty":
        if len(stk) ==0:
            print(1)
        else:
            print(0)
    elif T[0] == "top":
        if len(stk) ==0:
            print(-1)
        else:
            print(stk[-1])


#스택 기초 연습