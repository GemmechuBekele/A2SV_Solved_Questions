# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        idx = inorder.index(preorder[0])
        #left and rightt Inorder

        leftIn = inorder[:idx]
        rightIn = inorder[idx+1:]

        leftSize = len(leftIn)

        #left and rightt Preorder
        leftPreorder = preorder[1:leftSize + 1]
        rightPreorder = preorder[leftSize + 1:]

        root.left = self.buildTree(leftPreorder,  leftIn)
        root.right = self.buildTree(rightPreorder,  rightIn)

        return root
        