m,n = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
# x = sum((lst[:n]))
x = [abs(x) for x in lst[:n] if x <= 0]
print(x)