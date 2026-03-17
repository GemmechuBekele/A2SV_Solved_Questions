class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(l, r):
            if l == r:
                return nums[l]
            leftPick = nums[l]-winner(l+1, r)
            rightPick = nums[r]-winner(l, r-1)

            return max(leftPick, rightPick)
        res = winner(0, len(nums)-1)
        
        return res >= 0
        