using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public bool compare_words(string word, string comp) {
        int diff_count = 0;
        
        for(int i = 0; i < word.Length; i++) {
            if(word[i] != comp[i]) {
                diff_count++;
                
                if(diff_count > 1) return false;
            }
        }
        
        return diff_count == 1;
    }
    
    public int solution(string begin, string target, string[] words) {
        int answer = 0;
        
        Queue<(string word, int count)> queue = new Queue<(string, int)>();
        bool[] visited = new bool[words.Length];
        
        queue.Enqueue((begin, 0));
        
        while(queue.Count != 0) {
            var pair = queue.Dequeue();
            string word = pair.word;
            int count = pair.count;
            
            if(word == target) {
                answer = count;
                break;
            }
            
            for(int i = 0; i < words.Length; i++) {
                if(compare_words(word, words[i]) && !visited[i]) {
                    visited[i] = true;
                    queue.Enqueue((words[i], count + 1));
                }
            }
        }
        
        return answer;
    }
}