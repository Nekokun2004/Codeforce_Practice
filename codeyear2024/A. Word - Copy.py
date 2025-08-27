word = list(input())
countup = 0
countlow = 0
for i in word:
    if i.isupper():
        countup += 1
    else:
        countlow += 1
if countlow >= countup:
    print(''.join(word).lower())
else:
    print(''.join(word).upper())

