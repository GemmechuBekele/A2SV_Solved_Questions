class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        def backtrack():
            # 1. Base case (solution found)
            if len(path)==len(nums):
                result.append(path.copy())
                return

            # 2. Try all choices
            for n in nums:
                if n not in path:
                    path.append(n)
                    backtrack()
                    path.pop()
        backtrack()
        return result