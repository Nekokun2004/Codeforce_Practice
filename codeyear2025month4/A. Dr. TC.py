t = int(input())
for i in range(t):
    n = int(input())
    word = list(input())
    # print("list = ",word)
    count = 0
    for x in range(len(word)):
        if word[x] == '1':
            word[x] = '0'
            # print(word)
            count += word.count('1')
            word[x] = '1'
        else:
            word[x] = '1'
            # print(word)
            count += word.count('1')
            word[x] = '0'
    print(count)