n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
print(lst)
count = 0
index = 0
for i in range(n):
    if lst[i] > m:
        break
    count += lst[i]
    index += 1
    if i < n-1:
      lst[i+1] += lst[i]
    print(lst)
print(index,count)