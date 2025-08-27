n = int(input())
lst = list(map(int,input().split()))
lst.sort(reverse=True)
maxlst = lst[0]
count = 0
for i in lst[1:]:
   count += maxlst - i
print(count)
