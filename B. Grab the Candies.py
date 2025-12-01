import sys

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    lsta = list(map(int,input().split()))   
    sumlsta = sum(lsta)
    countMihai = sum([x for x in lsta if x % 2 == 0])
    countBianca = sum([x for x in lsta if x % 2 == 1])
    
    if countMihai > countBianca :
        out.append("YES")
    else:
        out.append("NO")
print("\n".join(out))
