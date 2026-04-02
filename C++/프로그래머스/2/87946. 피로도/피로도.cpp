#include <string>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    
    int og_k = k;
    int max_cnt = 0;
    
    vector<int> idxs(dungeons.size());
    iota(idxs.begin(), idxs.end(), 0);
    
    do {
        k = og_k;
        int cnt = 0;
        
        for(int i = 0; i < idxs.size(); i++) {
            vector<int> info = dungeons[idxs[i]];
            
            if(k >= info[0]) {
                k -= info[1];
                cnt++;
            }
        }
        max_cnt = max(max_cnt, cnt);
        
        if(max_cnt == dungeons.size()) break;
    } while(next_permutation(idxs.begin(), idxs.end()));
    
    answer = max_cnt;
    return answer;
}