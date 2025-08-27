def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    laptops = [tuple(map(int, input().split())) for _ in range(n)]
    laptops.sort(key=lambda x: x[0])
    for i in range(n - 1):
        if laptops[i][1] > laptops[i + 1][1]:
            print("Happy Alex")
            return
    print("Poor Alex")


if __name__ == "__main__":
    main()


# n = int(input())
# lst = [ list(map(int,input().split())) for _ in range(n)]
# # print(lst)
# lst.sort(key=lambda x : x[0])
# # print(lst)
# last_value = lst[-1][-1]
# reslut = [x[1] // x[0] for x in lst]
# # print(reslut)
# last_value = reslut[-1]
# if all(last_value >= x for x in reslut[:-1]):  
#     print("Poor Alex")
# else:
#     print("Happy Alex")