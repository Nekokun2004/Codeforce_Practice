def can_partition(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True  
    
    for num in nums:
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True  
    
    return dp[target]

def main():
    t = int(input())  
    for _ in range(t):
        n = int(input())  
        candies = list(map(int, input().split()))  
        total_weight = sum(candies)
        if total_weight % 2 != 0:
            print("NO")
            continue
        target = total_weight // 2
        if can_partition(candies, target):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()