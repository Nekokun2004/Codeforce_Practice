

t = int(input())
for _ in range(t):
    n = int(input())
    player = list(map(int,input().split()))
    onep = player.count(1)
    zerop = player.count(0)
    if onep == 0 or zerop == 0:
        print("YES")
    else:
        for i in range(len(player)-1):
            answer = True
            if player[i] == 0 :
                if player[i+1] == 0:
                    answer = False
                    break
            else:
                answer = True
        if answer:
            print("NO")
        else:
            print("YES")

