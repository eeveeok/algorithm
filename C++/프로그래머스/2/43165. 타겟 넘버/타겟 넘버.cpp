#include <vector>

using namespace std;

int dfs(int depth, int answer, vector<int> numbers, int target)
{
	if (depth == numbers.size())
	{
		if (answer == target) return 1;
		else return 0;
	}

	int number = numbers[depth];

	return dfs(depth + 1, answer + number, numbers, target) + dfs(depth + 1, answer - number, numbers, target);
}

int solution(vector<int> numbers, int target)
{
	int answer = 0;
	int num = numbers[0];

	answer = dfs(1, num, numbers, target) + dfs(1, -num, numbers, target);

	return answer;
}