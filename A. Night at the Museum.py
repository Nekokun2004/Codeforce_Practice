name = input().strip()  
strat = 'a'               
moves = 0

for ch in name:
    diff = abs(ord(ch) - ord(strat))
    moves += min(diff, 26 - diff)  
    strat = ch  

print(moves)
