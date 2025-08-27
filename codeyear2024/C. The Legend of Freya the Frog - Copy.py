t = int(input())
for i in range(t):
    x, y, k = map(int, input().split())
    moves_x = ((x + k) - 1) // k
    moves_y = ((y + k) - 1) // k
    if moves_x == moves_y:
        total_moves = (moves_x * 2 )
    else:
        total_moves = (max(moves_x, moves_y) * 2) - 1
        if moves_x < moves_y:
            total_moves = total_moves + 1

    print(total_moves)
