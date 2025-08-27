def solve():
    l,r = [int(x) for x in input().split()]
    count = 0
    nowX = l
    index = 1
    while True:
        count += 1
        nextval = nowX + index

        if nextval > r:
            break

        nowX = nextval
        index += 1
    print(count)

for _ in range(int(input())):
    solve()