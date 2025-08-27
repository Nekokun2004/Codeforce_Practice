import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    count1 = 1
    maxva = 1
    # print(lst)
    for i in range(n-1):
        # print(f"{lst[i]} and {lst[i+1]} == {abs(lst[i]-lst[i+1])}")
        if abs(lst[i]-lst[i+1]) <= k:
            count1 += 1
        else:
            maxva = max(maxva,count1)
            count1 = 1
    maxva = max(maxva,count1)
    
    out.append(len(lst)-maxva)
print("\n".join(map(str,out)))
 
    