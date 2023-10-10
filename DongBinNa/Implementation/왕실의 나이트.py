input_data = input()
# column = 가로 영어
column = int(ord(input_data[0])) - int(ord('a')) + 1
# row = 세로 숫자
row = int(input_data[1])

steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
cnt = 0
for step in steps:

    nr = row + step[0]
    nc = column + step[1]
    if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8:
        cnt += 1

print(cnt)
