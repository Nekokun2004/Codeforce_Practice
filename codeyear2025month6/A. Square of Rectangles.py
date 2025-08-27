import math

def can_form_square(rects):
    total_area = sum(l * b for l, b in rects)
    S = int(math.isqrt(total_area))
    if S * S != total_area:
        return False

    (l3, b3), (l2, b2), (l1, b1) = rects
    if b1 == b2 == b3 == S and l1 + l2 + l3 == S:
        return True
    if l1 == l2 == l3 == S and b1 + b2 + b3 == S:
        return True
    if b1 == S:
        rem_w = S - l1
        if rem_w > 0 and l2 == rem_w and l3 == rem_w and b2 + b3 == S:
            return True
    if l1 == S:
        rem_h = S - b1
        if rem_h > 0 and b2 == rem_h and b3 == rem_h and l2 + l3 == S:
            return True

    return False


t = int(input())
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    rects = sorted([(l1, b1), (l2, b2), (l3, b3)],key=lambda x: (x[0], x[1]))
    print("YES" if can_form_square(rects) else "NO")

