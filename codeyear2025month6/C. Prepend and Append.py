t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(input())
    count = 0
    while (lst[0] == '1' and lst[-1] == '0') or (lst[0] == '0' and lst[-1] == '1'):
        lst.pop(len(lst)-1)
        lst.pop(0)
        # print(lst)
        # break
        if len(lst) == 0:
            break
    print(len(lst))