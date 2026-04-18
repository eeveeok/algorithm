def solution(info, n, m):
    answer = 0
    
    INF = 10**9
    length = len(info)
    
    dp = [[INF] * n for _ in range(length+1)]
    dp[0][0] = 0
    
    for i in range(1, length+1):
        a_i, b_i = info[i-1]
        for prev_a in range(n):
            if dp[i-1][prev_a] >= m:
                continue
            
            new_a = prev_a + a_i
            if new_a < n:
                dp[i][new_a] = min(dp[i][new_a], dp[i-1][prev_a])
            
            new_b = dp[i-1][prev_a] + b_i
            if new_b < m:
                dp[i][prev_a] = min(dp[i][prev_a], new_b)
    
    answer = INF
    for i in range(n):
        if dp[length][i] < m:
            answer = min(answer, i)
    
    return answer if answer != INF else -1