def solution(prices):
    answer = []
    
    for i in range(len(prices) - 1):
        secs = 0
        for j in range(i+1, len(prices)):
            secs += 1
            if prices[i] > prices[j]:
                answer.append(secs)
                break
            elif j == len(prices) - 1:
                answer.append(secs)
    
    answer += [0]
    return answer