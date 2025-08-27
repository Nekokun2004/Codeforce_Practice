# first,last,random = map(str,[input(),input(),input()])
# count1 = {}
# count2 = {}
# for x in first:
#     if x not in count1:
#         count1[x]=1
#     else:
#         count1[x]+=1
# for x in last:
#     if x not in count1:
#         count1[x]=1
#     else:
#         count1[x]+=1
# for x in random:
#     if x not in count2:
#         count2[x]=1
#     else:
#         count2[x]+=1
# if count1 == count2:
#     print("YES")
# else:
#     print("NO")


from collections import Counter

def can_restore(guest: str, host: str, pile: str) -> bool:
    needed = Counter(guest + host)
    found = Counter(pile)
    print("needed =",needed)
    print("found = ",found)
    return needed == found

if __name__ == "__main__":
    guest = input().strip()
    host  = input().strip()
    pile  = input().strip()

    print("YES" if can_restore(guest, host, pile) else "NO")
