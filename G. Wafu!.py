import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))

    cost = 1
    while k > 0:
        lst.sort()
        # print(lst[0],"k = ", k )
        cost *= lst[0]
        # print("cost = ",cost)
        # print([x for x in range(1,lst[0])])
        lst += [x for x in range(1,lst[0])]
        lst.remove(lst[0])
        k-= 1
    print(lst)
    print(cost)
