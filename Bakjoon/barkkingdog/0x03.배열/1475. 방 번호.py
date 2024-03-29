T = input()

arr = [0] * 10

for i in T:
    arr[int(i)] += 1
    if i == '6' and arr[6] > arr[9]:
        arr[6] -= 1
        arr[9] += 1
    elif i == '9' and arr[6] < arr[9]:
        arr[6] += 1
        arr[9] -= 1
print(max(arr))

# 0으로 된 길이 10의 배열을 선언해준다.
# 입력받은 T에 대해 for문을 돌려주고, 이에 속한 arr값에 +1을 한다.
# 이때 6과 9는 같이 쓰일 수 있으므로 i가 6,9일때를 가정해서 풀어야한다.
# 여기서 문제는 6일때 9를 사용할 수 있는데, arr[6]>arr[9]라면 이미 6을 쓴 것이므로
# 6번째는 카운트하지 않고, 9번째만 +1을 더한다. 9일때도 이와같다.
# 이후 arr안에서 가장 큰 숫자를 출력해줘야한다.
# 가장 큰 숫자만큼 뭉치가 필요한 것이기 때문이다.