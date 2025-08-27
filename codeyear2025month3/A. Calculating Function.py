def func(n):
    if n % 2 == 0:
        return n // 2
    else:
       return -(n // 2) - 1



number = int(input())
print(func(number))
