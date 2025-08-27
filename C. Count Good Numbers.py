def count_good_numbers(l, r):
    from itertools import combinations

    # primes ตัวเล็กที่เราจะกรองออก
    small_primes = [2, 3, 5, 7]
    
    def count(x):
        res = 0
        for mask in range(1 << len(small_primes)):
            mul = 1
            bits = 0
            for i in range(len(small_primes)):
                if (mask >> i) & 1: 
                    mul *= small_primes[i]
                    bits += 1
            term = x // mul
            if bits % 2 == 1:
                res -= term
            else:
                res += term
        return res

    return count(r) - count(l - 1)

for i in range(int(input())):
    l,r = map(int,input().split())
    print(count_good_numbers(l,r))

