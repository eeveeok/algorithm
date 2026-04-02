#include <vector>
#include <queue>

using namespace std;

int solution(vector<vector<int>> maps)
{
	int answer = 0;

	queue<pair<int, int>> queue;

	int n = maps.size();
	int m = maps[0].size();

	//if (maps[n - 2][m -1] == 0 && maps[n - 1][m - 2] == 0) return -1;

	vector<vector<int>> dist(n, vector<int>(m, -1));
	int dx[4] = { -1, 0, 1, 0 };
	int dy[4] = { 0, 1, 0, -1 };

	dist[0][0] = 1;

	queue.push({ 0, 0 });

	while (!queue.empty())
	{
		int x = queue.front().first;
		int y = queue.front().second;

		queue.pop();

		for (int i = 0; i < 4; i++)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1 && dist[nx][ny] == -1)
			{
				dist[nx][ny] = dist[x][y] + 1;
				queue.push({ nx, ny });
			}
		}
	}

	answer = dist[n - 1][m - 1];

	return answer;
}