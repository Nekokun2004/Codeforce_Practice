import sys
import math

def fucn(x,y):
    if x>y:
        x,y = y,x
    if (x+1) * 2 >= y:
        return 1
    else:
        return 0 
    
input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    a,b,c,d = map(int,input().split())
    if a>c or b>d :
        out.append("NO")
        continue
    c -= a
    d -= b
    if fucn(a,b) and fucn(c,d):
        out.append("YES")
    else:
        out.append("NO")
print("\n".join(out))
