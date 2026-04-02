#include <vector>
#include <unordered_set>

using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    unordered_set<int> set;
    
    for(int num : nums)
    {       
        set.insert(num);
        
        if(set.size() == nums.size() / 2)
            break;
    }
    
    answer = set.size();
    
    return answer;
}