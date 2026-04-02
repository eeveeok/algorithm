#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int mod = 1000000007;
    set<pair<int, int>> obstacles;
    for (auto p : puddles) {
        obstacles.insert({p[0], p[1]});
    }
    
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    dp[1][1] = 1;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (obstacles.find({i, j}) != obstacles.end()) {
                dp[i][j] = 0;
                continue;
            }
            if (i > 1) {
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod;
            }
            if (j > 1) {
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % mod;
            }
        }
    }
    
    return dp[m][n];
}