def solution(s):
    answer = len(s)
    
    for n in range(1, len(s) + 1):
        temp = ''
        word = ''
        word_cnt = 1
        pre_word = ''
        
        for i in range(0, len(s), n):
            cur_word = s[i:i+n]
            
            if pre_word == cur_word:
                temp = temp[:-n] if word_cnt == 1 else temp[:-(n+len(str(word_cnt)))]
                word_cnt += 1
                word = str(word_cnt) + cur_word
            else:
                word_cnt = 1
                word = pre_word = cur_word
            
            temp += word
        
        answer = min(answer, len(temp))
            
    return answer