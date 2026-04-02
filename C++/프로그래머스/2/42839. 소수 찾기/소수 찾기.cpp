#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

bool isPrime(int num)
{
    if(num <= 1) return false;
    for(int i = 2; i * i <= num; i++)
    {
        if(num % i == 0) return false;
    }
    
    return true;
}

int solution(string numbers) {
    int answer = 0;
    set<int> nums;
    
    sort(numbers.begin(), numbers.end());
    
    do
    {
        for(int len = 1; len <= numbers.size(); len++)
        {
            string temp = numbers.substr(0, len);
            int n = stoi(temp);
            nums.insert(n);
        }
    } while(next_permutation(numbers.begin(), numbers.end()));
    
    for(int num : nums)
    {
        if(isPrime(num)) answer++;
    }
    
    return answer;
}