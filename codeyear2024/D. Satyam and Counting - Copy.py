t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        x,y = map(int, input().split())
    if n <= 3:
        print(0)
    else:
        print(n - 1)

# 18
# 0 0
# 0 1
# 2 1
# 4 0
# 4 1
# 5 1
# 6 0
# 6 1
# 7 0
# 7 1
# 8 1
# 9 1

# 5
# 1 0
# 1 1
# 3 0
# 5 0
# 2 1