n = int(input())
word = list(input())
count = 0
for index in range(n - 1):  
    if word[index] == word[index + 1]:
        count += 1

print(count)