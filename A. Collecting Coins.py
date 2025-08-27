import sys

def main():
    data = sys.stdin.read().split()  
    it = iter(data)
    t = int(next(it))  

    out = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        d = int(next(it))

        maxuse = max(a, b, c)
        need = (maxuse - a) + (maxuse - b) + (maxuse - c)
        total = a + b + c + d

        if total % 3 == 0 and need <= d:
            out.append("YES")
        else:
            out.append("NO")

    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
