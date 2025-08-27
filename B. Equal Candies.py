t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    minlst =  min(lst)
    sumlst = sum(lst) - (minlst*len(lst))
    print(sumlst)