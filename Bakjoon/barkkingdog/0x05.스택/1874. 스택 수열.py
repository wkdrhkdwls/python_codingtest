T = int(input())
stack = []
res = []
cnt = 1
flag = True

for i in range(T):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        res.append("+")
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        res.append("-")
    else:
        print("NO")
        flag = False
        break
if flag:
    for i in res:
        print(i)
