import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n,k,x = map(int,input().strip().split())
    num = k*(k+1)//2
    if num <= x <= k*((2*n)-k+1)//2: 
        out.append("YES")
    else:
        out.append("NO")
print("\n".join(out))
