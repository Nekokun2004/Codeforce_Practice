import sys

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    g = list(map(int, input().split()))
    g.sort(reverse=True) 
    ans = sum(g[0::2])
    out.append(ans)
# print(out)
        
print("\n".join(map(str,out)))