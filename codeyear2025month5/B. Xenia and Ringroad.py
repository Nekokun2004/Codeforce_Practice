n,m = map(int,input().split())
lst = list(map(int,input().split()))
count = 0
index = 1
if len(lst) > 1:
    count += lst[0] - 1
    for i in range(len(lst)-1):
        # print("i = ",i)
        # print("--------")
        # print("count =",count)
        if lst[i] > lst[i+1]:
            count += n - (lst[i] - lst[i+1])
        elif lst[i] < lst[i+1]:
            count += (lst[i+1] - lst[i])
        elif lst[i] == lst[i+1]:
            pass
else:
   count += lst[0] - 1

print(count)