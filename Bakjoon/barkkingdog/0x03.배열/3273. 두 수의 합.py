T = int(input())
nums = list(map(int, input().split()))
X = int(input())
cnt = 0

nums.sort()
for i in range(T):
    for j in range(i + 1, T):
        if nums[i] + nums[j] == X:
            cnt += 1
        if nums[i] + nums[j] > X:
            break
print(cnt)
