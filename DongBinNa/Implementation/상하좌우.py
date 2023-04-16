n = int(input())
moves = input().split()
x, y = 1, 1
move_direct = ["L", "R", "U", "D"]

for move in range(len(moves)):
    if moves[move] == move_direct[0]:
        if y - 1 == 0:
            continue
        else:
            y -= 1
    if moves[move] == move_direct[1]:
        if y + 1 == n + 1:
            continue
        else:
            y += 1
    if moves[move] == move_direct[2]:
        if x - 1 == 0:
            continue
        else:
            x -= 1
    if moves[move] == move_direct[3]:
        if x + 1 == n + 1:
            continue
        else:
            x += 1
print(x, y)
