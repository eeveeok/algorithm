#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;

    queue<int> q;
    vector<int> visited(edge.size() + 1, 0);

    visited[1] = 1;
    q.push(1);

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int i = 0; i < edge.size(); i++) {
            if (edge[i][0] != cur && edge[i][1] != cur) continue;

            int nxt = (edge[i][0] == cur) ? edge[i][1] : edge[i][0];

            if (!visited[nxt]) {
                visited[nxt] = visited[cur] + 1;
                q.push(nxt);
            }
        }
    }

    int max = *max_element(visited.begin(), visited.end());

    for (int n : visited) {
        if (n == max) answer++;
    }

    return answer;
}