n = int(input())
a = [int(x) for x in input().split()]
b = a.copy()
count = 0
index = 0
maxa = max(a)
max_index = a.index(maxa) 
while a[0] != max(a):
  a[max_index] = a[max_index-1]
  a[max_index-1] = max(b)
  max_index -= 1
  count += 1
mina = min(a)
min_index = len(a) - 1 - a[::-1].index(mina)
suma = count + (len(a) - min_index - 1)
print(suma)
