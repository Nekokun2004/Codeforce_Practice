for i in range(int(input())):
    n = int(input())
    lst1 = list(input())
    lst2 = list(input())
    answer = True
    for i in range(n):
        if (lst1[i] == 'R' and lst2[i] != 'R' ) or (lst2[i] == 'R' and lst1[i] != 'R' ):
            answer = False
            break
        elif (lst1[i] != 'R' and lst2[i] == 'R') or (lst2[i] != 'R' and lst1[i] == 'R'):
            answer = False
            break
    if answer:
        print("YES")
    else:
        print("NO")

