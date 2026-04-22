def solution(maps):
    answer = 0
    
    h = len(maps)
    w = len(maps[0])
    
    queue = []
    visited = [[-1] * w for _ in range(h)]
    
    dir_x = [0, 1, 0, -1]
    dir_y = [1, 0, -1, 0]
    
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        pair = queue.pop(0)
        org_x, org_y = pair[0], pair[1]
        
        for i in range(4):
            new_x = org_x + dir_x[i]
            new_y = org_y + dir_y[i]
            
            if 0 <= new_x < h and 0 <= new_y < w and maps[new_x][new_y] == 1 and visited[new_x][new_y] == -1:
                visited[new_x][new_y] = visited[org_x][org_y] + 1
                queue.append((new_x, new_y))
    
    answer = visited[-1][-1]
    
    return answer