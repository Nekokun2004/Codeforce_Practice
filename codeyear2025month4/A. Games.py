n = int(input())
Boxh = []
Boxa = []
for i in range(n):
    h,a = [int(x) for x in input().split()]
    Boxh.append(h)
    Boxa.append(a)
count = 0
for _ in Boxh:
    if _ in Boxa:
        count += Boxa.count(_)
print(count)