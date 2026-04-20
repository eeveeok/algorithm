def solution(priorities, location):
    answer = 0
    prt_tuple = [(i, v) for i, v in enumerate(priorities)]
    
    while prt_tuple:
        temp = prt_tuple.pop(0)
        
        if any(x[1] > temp[1] for x in prt_tuple):
            prt_tuple.append(temp)
        else:
            answer += 1
            if(location == temp[0]):
                break;
    
    return answer