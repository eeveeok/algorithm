def solution(s):
    answer = ''
    
    nxt_upper = True
    
    for ch in s:
        if nxt_upper:
            answer += ch.upper()
        else:
            answer += ch.lower();
        
        if ch == ' ':
            nxt_upper = True
        else:
            nxt_upper = False
    
    return answer