n,m = map(int,input().split())
count = 0
spot = n * m
for _ in range(min(n,m)):
    spot = n * m
    n -= 1
    m -= 1
    count += 1
    # print("spot = ",spot)
    # print("count = ",count)
if count % 2 == 1:
    print("Akshat")
else:
    print("Malvika")
