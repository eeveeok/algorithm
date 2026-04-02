#include <string>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

int solution(int N, int number) {
	int answer = -1;

    if (N == number) return 1;
    
	vector<set<int>> dp(9);
	
	dp[1] = { N };
	for (int i = 1; i < 8; i++)
	{
		int nextNumber = N * pow(10, i) + *dp[i].begin();

		dp[i + 1] = { nextNumber };
	}

	for (int i = 2; i < 9; i++)
	{
		for (int j = 1; j < i; j++)
		{
			int k = i - j;
			for (int a : dp[j])
			{
				for (int b : dp[k])
				{
					dp[i].insert(a + b);
					dp[i].insert(a - b);
					dp[i].insert(a * b);

					if(b != 0)
						dp[i].insert(a / b);

					if (dp[i].find(number) != dp[i].end())
					{
						return i;
					}
				}
			}
		}
	}

	return answer;
}