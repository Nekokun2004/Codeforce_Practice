#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int t;
    cin >> t;
    for (int test = 0; test < t; ++test) {
        int n;
        cin >> n;
        vector<long long> p(n);
        for (int i = 0; i < n; ++i) {
            cin >> p[i];
        }
        vector<long long> s(n);
        for (int i = 0; i < n; ++i) {
            cin >> s[i];
        }
        
        if (p[n-1] != s[0]) {
            cout << "No" << endl;
            continue;
        }
        
        bool possible = true;
        
        for (int i = 0; i < n-1; ++i) {
            if (gcd(p[i], s[i+1]) != p[n-1]) {
                possible = false;
                break;
            }
        }
        
        if (!possible) {
            cout << "No" << endl;
            continue;
        }
        
        for (int i = 1; i < n; ++i) {
            if (p[i] == 0 || p[i-1] % p[i] != 0) {
                possible = false;
                break;
            }
        }
        
        if (!possible) {
            cout << "No" << endl;
            continue;
        }
        
        for (int i = 0; i < n-1; ++i) {
            if (s[i] == 0 || s[i+1] % s[i] != 0) {
                possible = false;
                break;
            }
        }
        
        if (possible) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
    return 0;
}