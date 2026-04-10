def solution(begin, target, words):
    if target not in words:
        return 0;
    
    queue = [(begin, 0)]
    visited = set();
    visited.add(begin)
    
    while len(queue) > 0:
        pair = queue.pop()
        cur = pair[0]
        count = pair[1]
        
        if(cur == target):
            return count;
        
        for word in words:
            if(word not in visited):
                diff_count = sum(1 for a, b in zip(cur, word) if a != b)
                if diff_count == 1:
                    visited.add(word)
                    queue.append((word, count + 1))
                
    return 0