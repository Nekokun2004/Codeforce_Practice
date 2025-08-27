t = int(input())
for _ in range(t):
    s = input().strip()
    count = sum(1 for i in range(3) if s[i] == "abc"[i])
    print("YES" if count >= 1 else "NO")



# t = int(input())
# a = 'a'
# b = 'b'
# c = 'c'
# for _ in range(t):
#     lst = list(input())
#     if lst[0] == a and lst[1] == b:
#         pass
#     elif lst[0] == a and lst[1] == c:
#         lst[1] = b
#         lst[2] = c
#     elif lst[0] == b and lst[1] == a:
#         lst[0] = a
#         lst[1] = b
#     elif lst[0] == c and lst[2] == a:
#         lst[0] = a
#         lst[2] = c
#     elif lst[1] == c and lst[2] == b:
#         lst[1] = b
#         lst[2] = c
#     if "".join(lst) == "abc":
#         print("YES")
#     else:
#         print("NO")

#     # print(lst)