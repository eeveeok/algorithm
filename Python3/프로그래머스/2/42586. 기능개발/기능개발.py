import math

def solution(progresses, speeds):
    answer = []
    
    count = 0
    max_day = 0
    
    for p, s in zip(progresses, speeds):
        days = math.ceil((100 - p) / s)
        
        if count > 0 and days > max_day:
            answer.append(count)
            count = 0
            max_day = 0
        
        count += 1
        max_day = max(max_day, days);
        
    if count > 0:
        answer.append(count)
        
    return answer