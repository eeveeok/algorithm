#include <string>
#include <vector>

using namespace std;



vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    int total = brown + yellow;
    
    int row = 2;
    int col = 0;
    
    int brown_cnt, yellow_cnt;
    
    do
    {
        row++;
        col = total / row;
        
        brown_cnt = ((col - 1) * 2) + ((row - 1) * 2);
        yellow_cnt = (col - 2) * (row - 2);
    }
    while(brown_cnt != brown || yellow_cnt != yellow);
    
    answer.push_back(col);
    answer.push_back(row);
    
    return answer;
}