# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        maxNum = max(nums)
        idx = nums.index(maxNum)
        root = TreeNode(maxNum)

        leftPrefix = nums[:idx]
        rightPrefix = nums[idx+1:]

        root.left = self.constructMaximumBinaryTree(leftPrefix)
        root.right = self.constructMaximumBinaryTree(rightPrefix)

        return root