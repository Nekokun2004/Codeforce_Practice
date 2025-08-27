a, b, c = map(int, [input(), input(), input()])
# box = []
# box.append(a)
# box.append(b)
# box.append(c)
con = True
index = 0
if a == 1 and b == 1 and c == 1:
    sumbox = a + b + c
else:
    if (a, b, c).count(1) == 1:
        if a == 1:
            sumbox = (a + b)* c
        elif b == 1:
            if a < c:
                sumbox = (a + b)* c
            else:
                sumbox = a * (b + c)
        elif c == 1:
            sumbox = a * (b + c)
    elif a == 1 and b == 1:
        sumbox = (a + b) * c
    elif a == 1 and c == 1:
        sumbox = a + b + c
    elif b == 1 and c == 1:
        sumbox = a * (b + c)
    else:
        sumbox = a * b * c
print(sumbox)