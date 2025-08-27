x = list(map(int,input().split()))
x.sort()
c = x[-1] - x[0]
a = x[-1] - x[2] 
b = x[-1] - (c + a)
print(a,b,c) 