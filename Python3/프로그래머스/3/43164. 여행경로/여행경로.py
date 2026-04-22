def dfs(cur, path, dic, used, total):
    if len(path) == total:
        return True
    if cur not in dic:
        return False
    
    for i in range(len(dic[cur])):
        if used[cur][i]:
            continue
            
        used[cur][i] = True
        nxt = dic[cur][i]
        path.append(nxt)
            
        if(dfs(nxt, path, dic, used, total)): return True
            
        used[cur][i] = False
        path.pop()
    
    return False

def solution(tickets):
    answer = ["ICN"]
    
    dic = {}
    used = {}
    for t in tickets:
        if t[0] not in dic.keys():
            dic[t[0]] = [t[1]]
            used[t[0]] = [False]
        else:
            dic[t[0]].append(t[1])
            used[t[0]].append(False)
        
            dic[t[0]].sort()
    
    dfs("ICN", answer, dic, used, len(tickets) + 1)
    
    return answer