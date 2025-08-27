n = int(input())
for i in range(n):
    m = 0
    a1,a2,b1,b2 = [int(x) for x in input().split()]
    if a1 > b1 :
        m += 1 
    if a2 > b2:
        m += 1
    # if a1 > b1 and a1 > b2 and a2 > b1 and a2 > b2:
    #     m += 1
    if a1 > b2:
        m += 1
    if a2 > b1:
        m += 1
    print(m)

