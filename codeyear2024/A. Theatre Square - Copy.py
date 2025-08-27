import math

def cal(n, m, a):
   return math.ceil(m/a) * math.ceil(n/a) 
        
n,m,a = map(int, input().split())
rec = n*m
A = a*a
if A == 1:
    print(rec)
else:
    print(cal(n, m, a))
    