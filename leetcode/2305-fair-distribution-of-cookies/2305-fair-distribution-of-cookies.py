class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        best = float('inf')

        def dfs(i):
            nonlocal best

            if i == len(cookies):
                best = min(best, max(children))
                return

            for j in range(k):
                if children[j] + cookies[i] >= best:
                    continue

                children[j] += cookies[i]
                dfs(i + 1)

                children[j] -= cookies[i]

                if children[j] == 0:
                    break

        dfs(0)
        return best
            