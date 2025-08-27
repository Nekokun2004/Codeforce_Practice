from collections import defaultdict

t = int(input())
score = defaultdict(int)

for _ in range(t):
    name = input()
    score[name] += 1


winner = max(score, key=score.get)
print(winner)
