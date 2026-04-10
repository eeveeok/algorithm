def dfs(idx, op, numbers, target):
    if idx == len(numbers):
        return 1 if op == target else 0
    
    return (
        dfs(idx + 1, op + numbers[idx], numbers, target)
        + dfs(idx + 1, op - numbers[idx], numbers, target)
    )

def solution(numbers, target):
    answer = 0
    
    answer = (dfs(1, numbers[0], numbers, target)
    + dfs(1, -numbers[0], numbers, target))
    
    return answer