#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<string> vec;
map<string, vector<string>> graph;
map<string, vector<bool>> used;

bool dfs(string cur, vector<string> path, int totalTickets)
{
    if(path.size() == totalTickets)
    {
        vec = path;
        return true;
    }
    
    for(int i = 0; i < graph[cur].size(); i++)
    {
        if(!used[cur][i])
        {
            string temp = graph[cur][i];
            
            used[cur][i] = true;
            path.push_back(temp);
            
            if(dfs(temp, path, totalTickets)) return true;
            
            path.pop_back();
            used[cur][i] = false;
        }
    }
    
    return false;
}

vector<string> solution(vector<vector<string>> tickets)
{
    vector<string> answer;
    
    for(auto& t : tickets)
    {
        used[t[0]].push_back(false);
        graph[t[0]].push_back(t[1]);
        sort(graph[t[0]].begin(), graph[t[0]].end());
    }
    
    dfs("ICN", {"ICN"}, tickets.size() + 1);
    
    answer = vec;
              
    return answer;
}