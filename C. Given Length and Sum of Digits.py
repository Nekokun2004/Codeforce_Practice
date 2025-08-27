
m, s = map(int, input().split())
if (s == 0 and m > 1) or s > 9 * m:
    print("-1 -1")
    exit()


if s == 0 and m == 1:
    print("0 0")
    exit()


small = []
rem = s
for i in range(m):
    for d in range(0 if i else 1, 10):            
        if 0 <= rem - d <= 9 * (m - i - 1):
            small.append(str(d))
            rem -= d
            break
large = []
rem = s
for i in range(m):
    for d in range(9, -1, -1):
        if 0 <= rem - d <= 9 * (m - i - 1):
            large.append(str(d))
            rem -= d
            break

print("".join(small), "".join(large))
