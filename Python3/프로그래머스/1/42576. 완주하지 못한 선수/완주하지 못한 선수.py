def solution(participant, completion):
    count = {}
    
    for i, v in enumerate(participant):
        count[v] = count.get(v, 0) + 1;
        
        if(i != len(participant)-1):
            name = completion[i]
            count[name] = count.get(name, 0) - 1;
    
    answer = [k for k, v in count.items() if v == 1][0]
    
    return answer