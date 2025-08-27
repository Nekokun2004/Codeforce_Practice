def rank(rating):
    if rating < 1200:
        return "newbie"
    elif rating < 1400:
        return "pupil"
    elif rating < 1600:
        return "specialist"
    elif rating < 1900:
        return "expert"
    elif rating < 2100:
        return "candidate master"
    elif rating < 2400:
        return "master"
    else:
        return "grandmaster"
    
S, C, M, D = input().split()
C = int(C)
M = int(M)
D = int(D)
N = C + D

if N <= M or rank(N) == rank(M):
    print("Think about it, you can do it!")
else:
    print(rank(N))
