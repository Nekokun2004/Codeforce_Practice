k, l, m, n, d = map(int, [input(), input(), input(), input(), input()])

damage = 0
for i in range(1, d+1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0 :
        damage += 1
print(damage)