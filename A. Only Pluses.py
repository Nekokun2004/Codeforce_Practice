import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    lst = list(map(int,input().split()))
    for i in range(5):
        x = [x for x in range(3) if lst[x] == min(lst)]
        lst[x[0]] += 1
    # print(lst)
    count = 1
    for num in lst:
        count *= num
    print(count)
        