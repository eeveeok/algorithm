#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;

    unordered_set<string> set(phone_book.begin(), phone_book.end());

    for (string str : set)
    {
        for (int len = 0; len < str.length(); len++)
        {
            string prefix = str.substr(0, len);
            if (set.find(prefix) != set.end())
            {
                return false;
            }
        }
    }

    return answer;
}