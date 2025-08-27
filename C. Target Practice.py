t = int(input())
ring_score = [1, 2, 3, 4, 5]  

for _ in range(t):
    grid = [input().strip() for _ in range(10)]
    total = 0
    # print(grid)
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':
                ring = min(i, j, 9 - i, 9 - j)
                if ring < 5:
                    total += ring_score[ring]
    print(total)
