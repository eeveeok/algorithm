from itertools import product

def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    
    combination = []
    for i in range(1, len(words) + 1):
        temp = list(product(words, repeat = i))
        combination += [''.join(word) for word in temp]

    combination.sort()
    return combination.index(word) + 1