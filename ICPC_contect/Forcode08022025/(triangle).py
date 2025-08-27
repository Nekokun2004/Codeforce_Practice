lst = []
for i in range(int(input())):
    lst.append(int(input()))
lst.sort()
# print(lst)
if len(lst) > 2:
    if lst[0] + lst[1] > lst[-1]:
        print("no")
    else:
        print("yes")
else:
    print("no")