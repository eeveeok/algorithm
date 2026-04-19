def solution(bridge_length, weight, truck_weights):
    answer = 1
    
    time = 0
    cur_weights = 0
    enter_info = []
    
    while truck_weights:
        time += 1
        
        w = truck_weights[0]
        
        if enter_info and enter_info[0][1] + bridge_length == time:
            cur_weights -= enter_info.pop(0)[0]
        
        if cur_weights + w <= weight:
            enter_info.append((w, time))
            cur_weights += w
            truck_weights.pop(0)
    
    answer = time + bridge_length
    return answer
