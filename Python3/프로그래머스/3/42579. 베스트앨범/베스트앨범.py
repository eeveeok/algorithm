def solution(genres, plays):
    answer = []
    
    songs = {x : [] for x in genres}
    
    for i in range(len(plays)):
        songs[genres[i]].append((i, plays[i]))
    
    sorted_genres = sorted(songs.keys(), key=lambda x:
                           -sum(p[1] for p in songs[x]))
    
    for g in sorted_genres:
        temp = sorted(songs[g], key=lambda x: (-x[1], x[0]))
        
        answer.extend(x[0] for x in temp[:2])
        
    return answer