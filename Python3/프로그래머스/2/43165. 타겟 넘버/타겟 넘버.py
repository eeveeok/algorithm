def dfs(cur, op, numbers, target):
    if cur == len(numbers):
        return 1 if op == target else 0
    
    nxt = cur + 1;
    return dfs(nxt, op + numbers[cur], numbers, target) + dfs(nxt, op - numbers[cur], numbers, target)

def solution(numbers, target):
    answer = dfs(1, numbers[0], numbers, target) + dfs(1, -numbers[0], numbers, target)
    
    return answer