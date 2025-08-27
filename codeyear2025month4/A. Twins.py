num = int(input())
coin = [int(x) for x in input().split()]
coin.sort(reverse= True)
count = 0
index = 0
s_coin = sum(coin) / 2
if num > 1:
    while count <= s_coin  :
        count += coin[index]
        index += 1
    print(index)
else:
    print(1)
