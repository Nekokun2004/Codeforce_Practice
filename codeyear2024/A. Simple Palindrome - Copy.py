def generate_vowel_string(n):
    vowels = "aeiou"  
    result = ""
    for i in range(n):
        result += vowels[i % 5]
    vowel_count = {v: result.count(v) for v in vowels}
    sorted_result = ''.join(v * vowel_count[v] for v in vowels)
    
    return sorted_result
# อ่านจำนวนเคส
t = int(input())
for _ in range(t):
    n = int(input())
    print(generate_vowel_string(n))

# def solve(n):
#     dict = {"a":0,
#             "e":0,
#             "i":0,
#             "o":0,
#             "u":0
#             }
#     p = "aeiou"
#     curr = 0
#     ans = ""
#     for _ in range(n):
#         dict[p[curr]] += 1
#         curr += 1
#         if curr >= 5:
#             curr = 0
#     for k,v in dict.items():
#         print(k*v, end="")
#     print()
 
# t = int(input())
 
# for i in range(t):
#     n = int(input())
#     solve(n)