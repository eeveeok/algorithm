def solution(sizes):
    answer = 0
    
    sizes = [sorted(x) for x in sizes]
    max_width = 0
    max_height = 0
    
    for size in sizes:
        max_width = max(max_width, size[0])
        max_height = max(max_height, size[1])
    
    answer = max_width * max_height
    
    return answer