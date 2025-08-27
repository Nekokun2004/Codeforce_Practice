t = int(input())
for _ in range(t):
    n = int(input())
    lst1 = list(range(n,1,-1))
    lst1.insert(0,1)
    print(*lst1)
# print(1, *range(n, 1, -1))
# lst1[1:] = reversed(lst[1:])