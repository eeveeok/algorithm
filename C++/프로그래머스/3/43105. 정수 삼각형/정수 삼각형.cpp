#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle)
{
	int answer = 0;

	int h = triangle.size();

	for (int i = h - 1; i > 0; i--)
	{
		vector<int>& t1 = triangle[i];
		vector<int>& t2 = triangle[i - 1];

		for (int j = 0; j < t1.size() - 1; j++)
		{
			t2[j] += max(t1[j], t1[j + 1]);
		}
	}

	answer = triangle[0][0];

	return answer;
}