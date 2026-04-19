def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks += [distance]
    
    left, right = 1, distance
    
    while left <= right:
        mid = (left + right) // 2
        prev_rock = 0
        removed_rocks = 0
        
        for rock in rocks:
            if rock - prev_rock < mid:
                removed_rocks += 1
            else:
                prev_rock = rock
        
        if removed_rocks > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
        
    return answer