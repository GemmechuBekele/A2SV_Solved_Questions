# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both are None
        if not p and not q:
            return True
        
        #  one is None
        if not p or not q:
            return False
        
        # values are different
        if p.val != q.val:
            return False
        
        # check left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)