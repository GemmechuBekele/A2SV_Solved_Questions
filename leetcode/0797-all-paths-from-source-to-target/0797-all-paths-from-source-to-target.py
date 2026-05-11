class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []

        def dfs(node, path):

            # If we reached target node
            if node == n - 1:
                ans.append(path[:])   # copy path
                return

            # Visit neighbors
            for nei in graph[node]:
                path.append(nei)      # choose
                dfs(nei, path)        # explore
                path.pop()            # backtrack

        dfs(0, [0])

        return ans
        