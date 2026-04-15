class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        la = float("-inf")
        for i in range(k):
            la = nums[i]
        return la