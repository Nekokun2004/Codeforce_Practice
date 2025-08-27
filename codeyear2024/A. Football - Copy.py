def Aca (num):
    if len(num) < 7:  
        return "NO"
    for i in range(len(num) - 6):  
        if num[i:i+7] == [num[i]] * 7 or num[i:i+7] == [0] * 7:
            return "YES"
    return "NO"


num = list(input())
final = Aca(num)
print(final)


