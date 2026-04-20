def solution(arr):
    answer = []
    
    for e in arr:
        if answer and answer[-1] == e:
            answer.pop()
        
        answer.append(e)
    
    return answer