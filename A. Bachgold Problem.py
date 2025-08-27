n = int(input())
print(n // 2)
lst = []
for i in range(n//2):
    lst.append(2)
if n % 2 != 0 :
    lst[-1] += 1
print(*lst)
