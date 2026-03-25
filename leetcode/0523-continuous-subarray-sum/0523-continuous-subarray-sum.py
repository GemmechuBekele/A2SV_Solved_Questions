class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = 0
        total_seen = {0:-1}
        for i in range(n):
            prefix += nums[i]
            if k!=0:
                prefix %= k
            if prefix in total_seen:
                if i- total_seen[prefix] > 1:
                    return True
            else:
                total_seen[prefix] = i

        return False


        