num = int(input())
namewin = list(input())
Danik = namewin.count('D')
Anton = namewin.count('A')
if Danik == Anton :
    print("Friendship")
else:
    if Danik > Anton :
        print("Danik")
    else:
        print("Anton")