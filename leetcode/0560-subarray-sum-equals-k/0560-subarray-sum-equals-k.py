class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        prefix = {0:1}
        count = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            
            if prefixSum - k in prefix:
                count += prefix[prefixSum - k]
            
            if prefixSum in prefix:
                prefix[prefixSum] += 1
            else:
                prefix[prefixSum] = 1
        
        return count

        