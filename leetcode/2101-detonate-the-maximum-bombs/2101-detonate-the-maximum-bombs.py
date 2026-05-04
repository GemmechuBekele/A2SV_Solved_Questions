class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        n = len(bombs)
        
        # Build graph
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                
                dx = x1 - x2
                dy = y1 - y2
                
                if dx * dx + dy * dy <= r1 * r1:
                    graph[i].append(j)
        
        # BFS to count reachable bombs
        def bfs(start):
            visited = set([start])
            q = deque([start])
            
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            
            return len(visited)
        
        # Try starting from each bomb
        res = 0
        for i in range(n):
            res = max(res, bfs(i))
        
        return res
            