# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
       
        self.count = 0
        def pathCheck(node, currSum):
            if not node:
                return
            currSum += node.val

            if currSum == targetSum:
                self.count += 1
            pathCheck(node.left, currSum)
            pathCheck(node.right, currSum)

        def traverseTree(node):
            if not node:
                return

            pathCheck(node, 0)

            traverseTree(node.left)
            traverseTree(node.right)

        traverseTree(root)
        return self.count