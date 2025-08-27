word = input().strip('{}').split()
word = [w.replace(',', '') for w in word]   
print(len(set(word)))
