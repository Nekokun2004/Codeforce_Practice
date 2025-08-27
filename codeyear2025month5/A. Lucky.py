t = int(input())
for i in range(t):
    sixdigits = [int(x) for x in input()]
    # print("sixdigit = ",sixdigits)
    # print("digitfirst = ",sixdigits[0:3])
    # print("digitsecond = ",sixdigits[3:6])
    sumfirst = sum(sixdigits[0:3])
    sumsecond = sum(sixdigits[3:6])
    if sumfirst == sumsecond :
        print("YES")
    else:
        print("NO")