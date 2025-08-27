n = int(input())

for i in range(n):
    count = 0
    maxva = 0
    lst = list(map(int,input().split()))
    num = lst[0]
    lst = lst[1:]
    for i in lst[::-1]:
        if i >= maxva:
            count += 1
        maxva = max(maxva,i)
    print(count)
