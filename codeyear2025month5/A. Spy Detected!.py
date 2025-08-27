t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    count = [x for x in range(len(lst)) if lst.count(lst[x]) == 1]
    count = int(''.join(map(str,count)))
    print(count+1)