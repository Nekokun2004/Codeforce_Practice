n = int(input())
name_dict = {}

for _ in range(n):
    word = input()
    if word not in name_dict:
        print("name_dict = ",name_dict)
        name_dict[word] = 0
        print("OK")
    else:
        print("name_dict = ",name_dict)
        name_dict[word] += 1
        new_name = word + str(name_dict[word])
        print(new_name)
