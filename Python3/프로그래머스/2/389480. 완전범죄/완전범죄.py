def solution(info, n, m):
    answer = -1

    visited = set()
    
    def dfs(cur = 0, signA = 0, signB = 0):
        nonlocal answer, n, m
        
        if signA >= n or signB >= m:
            return
        
        if (signA, signB, cur) in visited:
            return 
        
        visited.add((signA, signB, cur))
        
        if cur == len(info):
            answer = signA if answer == -1 else min(answer, signA)
            return
        
        dfs(cur + 1, signA + info[cur][0], signB)
        dfs(cur + 1, signA, signB + info[cur][1])
    
    dfs()
    
    return answer