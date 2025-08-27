from collections import Counter

t = int(input())
for _ in range(t):
    word = list(input())
    counterword = Counter(word)
    # print(counterword)

    print(max(counterword.items(),key=lambda x : x[1])[0])
