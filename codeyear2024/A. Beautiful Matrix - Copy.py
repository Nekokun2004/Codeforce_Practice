Box = []
for i in range(5):
    row = list(map(int, input().split()))
    Box.append(row)
for i in range(5):
    for j in range(5):
        if Box[i][j] == 1:
            moves = abs(i - 2) + abs(j - 2)
            print(moves)
            break

