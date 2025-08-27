def has_unique_digits(year):
    return len(set(str(year))) == len(str(year))

def next_beautiful_year(y):
    y += 1
    while not has_unique_digits(y):
        y += 1
    return y

y = int(input())
print(next_beautiful_year(y))
