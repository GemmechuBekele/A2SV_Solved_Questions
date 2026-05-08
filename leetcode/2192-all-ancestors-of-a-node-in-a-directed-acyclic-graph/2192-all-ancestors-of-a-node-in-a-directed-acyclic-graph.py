class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
         # graph[u] = all neighbors of u
        graph = [[] for _ in range(n)]
        
        # indegree[i] = number of incoming edges
        indegree = [0] * n
        
        # Build graph
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # ancestors[i] = set of ancestors of node i
        ancestors = [set() for _ in range(n)]
        
        # Queue for topological sort
        q = deque()
        
        # Nodes with indegree 0
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            
            # Visit neighbors
            for v in graph[u]:
                
                # u itself is an ancestor of v
                ancestors[v].add(u)
                
                # all ancestors of u are also ancestors of v
                ancestors[v].update(ancestors[u])
                
                # remove edge u -> v
                indegree[v] -= 1
                
                # if no incoming edges left
                if indegree[v] == 0:
                    q.append(v)
        
        # convert sets to sorted lists
        result = []
        
        for s in ancestors:
            result.append(sorted(list(s)))
        
        return result

        