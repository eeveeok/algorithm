def solution(n, times):
    left, right = 1, max(times) * n   # 최대 시간은 가장 느린 심사관이 모두 처리
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // t for t in times)
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer