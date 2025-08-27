import sys

lst = {}
for line in sys.stdin:
    a,b,c,d = line.split()
    b = int(b)
    c = int(c)
    d = int(d)
    b += c * 30
    b += (d *12)*30
    lst[a] = b
print(lst)
lst = sorted(lst.items(), key=lambda x:x[1])
print(lst[0][0])
print(lst[-1][0])
