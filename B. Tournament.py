t = int(input())
for _ in range(t):
    n,j,k = map(int,input().split())
    lst = list(map(int,input().split()))
    maxlst = max(lst)
    Chosen = lst[j-1]
    # print("Chosen = ",Chosen )
    # print(Chosen,"--------")
    
    # lst.sort()
    # x = [i for i,x in enumerate(lst) if x == Chosen]
    # x1 = int(x[-1])
    # print(x)
    # print(x1)
    if k > 1 or Chosen == maxlst:
        print("YES")
    else:
        print("NO")