class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        def backtrack(path):
            if len(path) == n:
                ans.append(path)
                return
            for ch in ["a", "b", "c"]:
                if path and path[-1] == ch:
                    continue
                backtrack(path + ch)

        backtrack("")

        if k > len(ans):
            return ""
        return ans[k-1]
            
        