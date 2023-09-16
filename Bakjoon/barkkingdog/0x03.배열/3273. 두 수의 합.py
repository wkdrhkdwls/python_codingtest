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

# 다시 풀어봐야하는 문제다. 해결은 했는데 시간이 계속 초과된다.
# 우선 지금 푼 방식으로 설명해보겠다.
# T, nums리스트, X 값을 받고, 맞는 값을 체크해줄 cnt로 값을 새긴다. 그 후 nums 리스트를 오름차순으로 섞는다.
# 이중 for문을 사용하여 만약 nums[i] + nums[j] == X이면 cnt값을 1씩 늘려간다.
# 오름차순으로 nums가 나열되어있기 때문에, 계속 반복하며 두 값이 X가 넘어가면 반복문을 탈출한다.
