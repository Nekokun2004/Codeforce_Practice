import sys

n = 0
lst = []
for line in sys.stdin:
    line = list(map(int,line.split()))
    lst += line
lst = lst[1:]
reversed_lst = [int(str(abs(n))[::-1]) * (-1 if n < 0 else 1) for n in lst]
for i in reversed_lst:
    print(i)
    
    
    
