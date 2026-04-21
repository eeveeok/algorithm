import math

def solution(clothes):
    answer = 1
    
    comb_dict = {x[1] : 1 for x in clothes}
    
    for c in clothes:
        comb_dict[c[1]] = comb_dict.get(c[1], 0) + 1
        
    answer = math.prod(comb_dict.values()) - 1
    
    return answer