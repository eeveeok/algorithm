using System;

public class Solution {
    public void dfs(int cur, int[,] computers, bool[] visited) {
        visited[cur] = true;
        
        for(int i = 0; i < computers.GetLength(0); i++) {
            if(computers[cur, i] == 1 && !visited[i]) {
                dfs(i, computers, visited);
            }
        }
    }
    
    public int solution(int n, int[,] computers) {
        int answer = 0;
        
        bool[] visited = new bool[n];
        
        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                dfs(i, computers, visited);
                answer++;
            }
        }
        
        return answer;
    }
}