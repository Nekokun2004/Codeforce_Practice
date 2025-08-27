n, m, a, b = map(int, input().split())
cost1 = n * a
cost2 = ((n + m - 1) // m) * b
min_cost = float('inf')
for k in range(n // m + 1):
    total_cost = k * b + (n - k * m) * a
    min_cost = min(min_cost, total_cost)
print(min(cost1, cost2, min_cost))

# def fucn1(n,a):
#     cost0 = n * a
#     return cost0

# def fucn2(n,m,a,b):
#     cost1 = -(-n//m) * b
#     return cost1

# def fucn3(n,m,a,b): 
#     cost2 = ((n//m) * b)
#     n = n % m
#     cost2 += n * a
#     return cost2

# n, m, a, b = map(int,input().split())
# print(min(fucn1(n,a),fucn2(n,m,a,b),fucn3(n,m,a,b)))