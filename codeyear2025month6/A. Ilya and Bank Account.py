n = input()
if int(n) >= 0:
    print(n)
else:
    lst = list(n)
    if lst[-1] > lst[-2]:
        lst.pop(len(lst)-1)
    elif lst[-1] < lst[-2]:
        lst.pop(len(lst)-2)
    else:
        lst.pop(len(lst)-1)
    # print("lst = ",lst)
    answer = "".join(lst)

    print(int(answer))