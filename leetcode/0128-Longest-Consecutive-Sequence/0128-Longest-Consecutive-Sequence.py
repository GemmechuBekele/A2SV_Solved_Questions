class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0
        if n == 0:
            return longest
        
        setNums = set(nums)
        
        for num in setNums:
            count = 1
            if num-1 not in setNums:
                current = num
                while current + 1 in setNums:
                    current += 1
                    count += 1
                longest = max(longest, count)
        return longest