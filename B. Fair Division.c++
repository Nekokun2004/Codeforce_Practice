#include <iostream>
#include <vector>
using namespace std;

// ฟังก์ชันตรวจสอบว่าสามารถแบ่งลูกอมให้ได้น้ำหนัก target หรือไม่
bool canPartition(vector<int>& nums, int target) {
    vector<bool> dp(target + 1, false);
    dp[0] = true; // น้ำหนัก 0 สามารถทำได้เสมอ (ไม่เลือกอะไรเลย)
    
    for (int num : nums) {
        for (int i = target; i >= num; --i) {
            if (dp[i - num]) {
                dp[i] = true; // ถ้าทำน้ำหนัก i - num ได้ เพิ่ม num เข้าไปก็ทำ i ได้
            }
        }
    }
    return dp[target];
}

int main() {
    int t;
    cin >> t; // อ่านจำนวน test cases
    
    for (int test = 0; test < t; ++test) {
        int n;
        cin >> n; // อ่านจำนวนลูกอม
        vector<int> candies(n);
        int total_weight = 0;
        
        // อ่านน้ำหนักลูกอมและคำนวณน้ำหนักรวม
        for (int i = 0; i < n; ++i) {
            cin >> candies[i];
            total_weight += candies[i];
        }
        
        // ถ้าน้ำหนักรวมเป็นเลขคี่ แบ่งไม่ได้
        if (total_weight % 2 != 0) {
            cout << "NO" << endl;
            continue;
        }
        
        // คำนวณน้ำหนักเป้าหมาย และตรวจสอบด้วย DP
        int target = total_weight / 2;
        if (canPartition(candies, target)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}