def solution(nums):
    answer = 0
    
    n = len(nums)
    pokemon = set()
    
    for e in nums:
        pokemon.add(e)
        
        if len(pokemon) == n / 2:
            break;
    
    answer = len(pokemon)
    return answer