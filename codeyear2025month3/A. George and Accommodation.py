room = int(input())
count = 0
for i in range(room):
  p,q = [int(x) for x in input().split()]
  if p <= q-2:
    count += 1
print(count)
  