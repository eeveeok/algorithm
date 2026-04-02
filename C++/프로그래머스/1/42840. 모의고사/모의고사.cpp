#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    vector<int> fisrt = {1, 2, 3, 4, 5};
    vector<int> second = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    vector<int> ansCnt(3, 0);
    
    for(int i = 0; i < answers.size(); i++)
    {
        if(answers[i] == fisrt[i % fisrt.size()]) ansCnt[0]++;
        if(answers[i] == second[i % second.size()]) ansCnt[1]++;
        if(answers[i] == third[i % third.size()]) ansCnt[2]++;
    }
    
    int res = *max_element(ansCnt.begin(), ansCnt.end());
    
    for(int i = 0; i < 3; i++)
    {
        if(res == ansCnt[i])
            answer.push_back(i + 1);
    }
    
    return answer;
}