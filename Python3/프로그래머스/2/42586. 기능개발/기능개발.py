def solution(progresses, speeds):
    answer = []
    
    size = len(progresses)
    completed = [False] * size
    
    while any(x < 100 for x in progresses):
        dayily_cplt = 0
        for i in range(size):
            is_prev_all_cplt = all(completed[:i])
            
            if completed[i]:
                if is_prev_all_cplt and dayily_cplt > 0:
                    dayily_cplt += 1
                    print(i, dayily_cplt)
                continue
            
            progresses[i] += speeds[i]
            
            if progresses[i] >= 100:
                completed[i] = True
                if is_prev_all_cplt:
                    dayily_cplt += 1
        
        if dayily_cplt > 0:
            answer.append(dayily_cplt)
        
    return answer