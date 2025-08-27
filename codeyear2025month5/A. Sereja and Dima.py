n = int(input())
cards = list(map(int, input().split()))

left = 0
right = n - 1
Sereja = 0
Dima = 0
turn = 0  
while left <= right:
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1

    if turn % 2 == 0:
        Sereja += chosen
    else:
        Dima += chosen

    turn += 1

print(Sereja, Dima)
