n = int(input())
all = list(map(int,input().split()))
# print(all)
lst = []
lownum = []
count = 0
index = 0
if n > 1:
    for i in range(len(all)):
        if len(lst) == 0:
            lst.append(all[i])
        elif all[i] > lst[-1] :
            lst.append(all[i])
            count += 1
        elif all[i] < lst[0]:
            lst.insert(0,all[i])
            count += 1
    # print(lst)
    print(count)
else:
    print(0)
# print(lst)

