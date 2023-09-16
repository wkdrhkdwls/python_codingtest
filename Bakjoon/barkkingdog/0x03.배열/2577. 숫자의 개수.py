A = int(input())
B = int(input())
C = int(input())

res = list(str(A*B*C))

for i in range(10):
    print(res.count(str(i)))

# 각각 A,B,C를 숫자로 입력받는다.
# 문자열의 형태로 A*B*C 값을 리스트에 저장하고 count함수로 각 자리수에 속한 값을 찾아낸다.