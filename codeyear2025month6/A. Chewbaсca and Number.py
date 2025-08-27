def transform_number(x):
    digits = list(str(x))
    n = len(digits)
    for i in range(n):
        digit = int(digits[i])
        inverse = 9 - digit
        if i == 0 and inverse == 0:
            continue
        if inverse < digit:
            digits[i] = str(inverse)
    return str(int(''.join(digits)))


x = int(input())
print(transform_number(x))