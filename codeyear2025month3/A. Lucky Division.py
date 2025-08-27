def is_lucky_number(n):
    return set(str(n)) <= {'4', '7'}

def is_almost_lucky(n):
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    
    for lucky in lucky_numbers:
        if n % lucky == 0:  
            return "YES"
    
    return "NO"


n = int(input())
print(is_almost_lucky(n))
