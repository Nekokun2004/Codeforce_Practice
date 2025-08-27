number = int(input())
juc = [int(x) for x in input().split()]
aver = 0
for i in juc:
  aver += i
aver = aver / number
print(f"{aver:.14f}")