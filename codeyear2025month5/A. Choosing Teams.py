n,k = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

many = n // 3
count = many
loccount = many * 3
for i in range(n):
    result = 5 - lst[i]
    lst[i] = result
index = loccount - 1
# print("many = ",many)
for x in range(many):
    # print("index = ",index)
    # print(f"{lst[index]} , {lst[index-2]}")
    if lst[index] < k :
        count -= 1
    else:
        break
    index -= 3

print(count)
# print(lst)
