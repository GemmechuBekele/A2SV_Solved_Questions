class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        new = {}

        for num in nums:
            if num not in new:
                new[num] = 1

            else:
                return True

        return False
        