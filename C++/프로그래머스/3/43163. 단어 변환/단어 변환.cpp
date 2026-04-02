#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int mismatchedCount(string begin, string cur)
{
    int cnt = 0;
    
    for(int i = 0; i < begin.length(); i++)
    {
        if(begin[i] != cur[i])
        {
            cnt++;
        }
    }
    
    return cnt;
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    int size = words.size();
    
    queue<pair<string, int>> q;
    vector<bool> visited(size, false);
    
    q.push({begin, 0});
    
    while(!q.empty())
    {
        string word = q.front().first;
        int cnt = q.front().second;
        q.pop();
        
        if(word.compare(target) == 0) 
        {
            answer = cnt;
            break;
        }
        
        for(int i = 0; i < size; i++)
        {
            string cur = words[i];
            
            if(!visited[i] && mismatchedCount(word, cur) == 1)
            {
                visited[i] = true;
                q.push({cur, cnt + 1});
            }
        }
    }
    
    return answer;
}