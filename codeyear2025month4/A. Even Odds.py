def pud(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n // 2 + 1

n,k = [int(x) for x in input().split()]
index = 1
if k <= pud(n) :
    count = k*2 - 1
    print(count)
else:
    count = (k-pud(n))*2
    print(count)
