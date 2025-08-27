t = int(input())
D = 0
for i in range(t):
    n = int(input())
    D += n//4
    over = n % 4
    if over > 0:
        D += over//2
    print(D)
    D = 0

