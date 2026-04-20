def solution(name):
    answer = sum(min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name)
    n = len(name)
    
    move = n - 1
    
    for i in range(n):
        next = i + 1
        
        while next < n and name[next] == 'A':
            next += 1
            
        move = min(move, i + (n - next) + min(i, n - next))
    
    answer += move
    return answer