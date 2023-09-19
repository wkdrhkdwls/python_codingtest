N = int(input())

cnt = 0
for i in range(N):
    T = input()
    stack = []

    for j in T:
        if len(stack) == 0:
            stack.append(j)
        else:
            if j == "A":
                if stack[-1] == "A":
                    stack.pop()

                elif stack[-1] == "B":
                    stack.append(j)
            else:
                if stack[-1] == "B":
                    stack.pop()

                elif stack[-1] == "A":
                    stack.append(j)

    if len(stack) == 0:
        cnt +=1
print(cnt)

