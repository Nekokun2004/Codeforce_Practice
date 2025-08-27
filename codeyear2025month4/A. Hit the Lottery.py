dollars = int(input())
count_h = dollars // 100
dollars = dollars % 100
count_q = dollars // 20
dollars = dollars % 20
count_d = dollars // 10
dollars = dollars % 10
count_f = dollars // 5
dollars = dollars % 5
count_n = dollars // 1
sumcount = count_h + count_q + count_d + count_f + count_n
print(sumcount)
