def max_books(n, t, a):
    left = 0
    total_time = 0
    max_count = 0

    for right in range(n):
        total_time += a[right] 
        while total_time > t:
            total_time -= a[left]
            left += 1

        max_count = max(max_count, right - left + 1)

    return max_count

if __name__ == "__main__":
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_books(n, t, a))

# def positionmin(n,lst):
#     Box = {}
#     for i in range(n-1):
#         Box[i] = lst[i]+lst[i+1]
#         if i == n-2:
#             Box[i+1] = lst[-1]+lst[0]
#     x = dict(sorted(Box.items(), key=lambda item:item[1]))
#     x = next(iter(x))
#     return x



# n,t = map(int,input().split())
# lst = list(map(int,input().split()))
# if n > 1:
#    x = positionmin(n,lst)
# else:
#     x = min(lst)
#     x = [i for i in range(n) if lst[i] == x]
#     x = x[0]
# # print(x)
# # x = min(lst)
# # x = [i for i in range(n) if lst[i] == x]
# # x = x[0]
# # # print("x =",x)
# index = x
# count = 0
# count_number = 0
# if sum(lst) > t:
#     while count < t:
#         # print("lst[index] = ",lst[index])
#         # print("index = ",index)
#         count += lst[index]
#         count_number += 1
#         if count > t:
#             count -= lst[index]
#             index -= 1
#             count_number -= 1
#             break
#         else:
#             index += 1
#         # print("index = ",index)
#         if index > n-1:
#             index = 0
#         # print("count = ",count)
#         # print("coint number = ",count_number,"\n")
#     print(count_number)
# else:
#     print(n)