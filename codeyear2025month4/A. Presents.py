n = int(input())
p = [int(x) for x in input().split()]
p1 = p.copy()
Box = []
index = 1
for i in range(len(p)):
  if p[i] == index:
    index += 1 
  else:
    cl = p[i]
    p1[cl-1] = i+1
    index += 1
print(*p1)

