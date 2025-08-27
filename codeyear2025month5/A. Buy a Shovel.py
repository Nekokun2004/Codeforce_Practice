k,r = map(int,input().split())
count = 1
new = 0
if k % 10 == r or k % 10 == 0:
    print(1)
else:
# if k % 10 != r:
    while new % 10 != r :
        count += 1
        new = k * count
        if new % 10 == 0:
            break
    print(count)
# elif k % 10 == r:
#     print(1)
