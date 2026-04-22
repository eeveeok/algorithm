def dfs(cur, n, computers, visited):
    for i in range(n):
        if computers[cur][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i, n, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = True
            dfs(i, n, computers, visited)
    
    return answer