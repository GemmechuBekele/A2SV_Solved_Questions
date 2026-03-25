class TreeNode:
    def __init__(self, data, childreen=[]):
        self.data = data
        self.childreen = childreen

    def __str__(self, level=0):
        ret = " "*level + str(self.data)+"\n"
        for child in self.childreen:
            ret += child.__str__(level+1)
        return ret
    
    def addChildreen(self, TreeNode):
        self.childreen.append(TreeNode)

tree = TreeNode("Grandpa", [])
dad = TreeNode("Father", [])
mum = TreeNode("Mother", [])
tree.addChildreen(dad)
tree.addChildreen(mum)
son = TreeNode("son", [])
daughter = TreeNode("daughter", [])
dad.addChildreen(son)
dad.addChildreen(daughter)
mum.addChildreen(son)
mum.addChildreen(daughter)
print(tree)
