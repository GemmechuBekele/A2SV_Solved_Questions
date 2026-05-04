class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        color = [-1] * n  
        
        for start in range(n):
            if color[start] != -1:
                continue
            
            queue = deque([start])
            color[start] = 0
            
            while queue:
                u = queue.popleft()
                
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u] 
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False   
        
        return True