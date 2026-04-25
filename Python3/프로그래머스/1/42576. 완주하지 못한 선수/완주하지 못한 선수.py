def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i, v in enumerate(completion):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]