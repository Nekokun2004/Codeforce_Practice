t = int(input())
for _ in range(t):
    word = list(input())
    if len(word) % 2 == 1:
        print("NO")
    elif [x for x in word if word.count(x) == 1]:
        print("NO")
    else:
        answer = True
        halfword = len(word)//2
        for i in range(1,len(word)//2 + 1):
                # print(f"word[-i] = {word[-i]} and word[halfword-i] = {word[halfword-i]} ")
            if word[-i] == word[halfword-i] :
                answer = True
            else:
                answer = False
                break
        if answer:
            print("YES")
        else:
            print("NO")