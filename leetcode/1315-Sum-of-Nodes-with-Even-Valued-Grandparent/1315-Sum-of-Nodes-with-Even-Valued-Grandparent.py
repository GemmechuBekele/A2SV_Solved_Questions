class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def evenValue(child, parent, grandpa):
            if not child:
                return
            if grandpa and grandpa.val % 2 == 0:
                self.total += child.val

            evenValue(child.left, child, parent)
            evenValue(child.right, child, parent)

        evenValue(root, None, None)
        return self.total