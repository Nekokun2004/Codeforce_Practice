word = input()

if word.isupper() or (word[0].islower() and word[1:].isupper()):
    result = []
    for ch in word:
        if ch.islower():
            result.append(ch.upper())
        else:
            result.append(ch.lower())
    print(''.join(result))
else:
    print(word)
