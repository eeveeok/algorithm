from queue import Queue

def solution(maps):
    m = len(maps)          # 세로 길이 (행 수)
    n = len(maps[0])       # 가로 길이 (열 수)
    
    queue = Queue()
    queue.put((1, 1))
    
    visited = [[-1] * (n + 2) for _ in range(m + 2)]
    visited[1][1] = 1
    
    dirx = [1, 0, -1, 0]
    diry = [0, 1, 0, -1]
    
    while not queue.empty():
        x, y = queue.get()
        for i in range(4):
            nx, ny = x + dirx[i], y + diry[i]
            if 1 <= nx <= m and 1 <= ny <= n and visited[nx][ny] == -1 and maps[nx-1][ny-1] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.put((nx, ny))
    
    return visited[m][n]