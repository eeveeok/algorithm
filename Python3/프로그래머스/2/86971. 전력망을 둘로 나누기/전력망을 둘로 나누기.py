def dfs(cur, info, visited):
    visited[cur] = True
    
    for nxt in info[cur]:
        if not visited[nxt]:
            dfs(nxt, info, visited)

def solution(n, wires):
    min_diff = n
    
    for w in wires:
        temp = [x for x in wires if x != w]
        
        info = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        
        for t in temp:
            info[t[0]].append(t[1])
            info[t[1]].append(t[0])
        
        dfs(1, info, visited)
        count = visited.count(True)
        
        min_diff = min(min_diff, abs(count - (n - count)))
        
    return min_diff