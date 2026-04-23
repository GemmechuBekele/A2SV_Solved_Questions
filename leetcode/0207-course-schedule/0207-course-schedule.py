class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cycle = False
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        visiting = set()
        visited = set()
        def dfs(node):
             nonlocal cycle
             if node in visiting:
                cycle = True
                return
            
             if node in visited:
                return
            
             visiting.add(node)

             for nei in graph[node]:
                dfs(nei)
            
             visiting.remove(node)
             visited.add(node)

        for i in range(numCourses):
            if i not in visited:
                dfs(i)
            if cycle:
                return False

        return True
        