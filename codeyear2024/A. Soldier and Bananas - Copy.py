k,n,w = map(int,input().split())
for i in range(w):
    Banana = k * (i+1)
    n = n - Banana
if n > 0:
    print(0)
else:
    print(abs(n))