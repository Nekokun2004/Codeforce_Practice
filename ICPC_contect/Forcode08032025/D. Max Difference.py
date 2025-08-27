import sys

lst = []
for line in sys.stdin.readlines():
   
   line = list(map(int,line.split()))
   lst += line
   
print(max(lst) - min(lst))