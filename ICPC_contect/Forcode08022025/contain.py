import sys

for line in sys.stdin:
    # line = sys.stdin.readline()
    a, b = map(int, line.strip().split())
    lst = [x for x in range(1,b+1) if str(a) in str(x)]
    print(len(lst))