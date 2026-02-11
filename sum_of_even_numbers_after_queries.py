class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        result = []
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num

        for val, idx in queries:
            old = nums[idx] 
            new = old + val

            if old % 2 == 0:
                even_sum -= old
            if new % 2 == 0:
                even_sum += new

            nums[idx] = new
            result.append(even_sum)
                
        return result