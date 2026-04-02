#include <string>
#include <vector>

using namespace std;

void dfs(int cur, vector<vector<int>> computers, vector<bool>& visited);

int solution(int n, vector<vector<int>> computers)
{
	int answer = 0;
	vector<bool> visited(n, false);

	for (int i = 0; i < n; i++)
	{
		if (!visited[i])
		{
			answer++;
			dfs(i, computers, visited);
		}
	}

	return answer;
}

void dfs(int cur, vector<vector<int>> computers, vector<bool>& visited)
{
	visited[cur] = true;

	for (int nxt = 0; nxt < computers.size(); nxt++)
	{
		if (!visited[nxt] && computers[cur][nxt] == 1)
		{
			dfs(nxt, computers, visited);
		}
	}
}