class Solution:
    def isValidBST(self, root:Optional[TreeNode])->bool:
        return self.valid(root,float('-inf'),float('inf'))
    def valid(self, node, lower, upper):
        if node is None:
            return True

        val = node.val
        if val <= lower or val >= upper:
            return False

        if not self.valid(node.left, lower, val):
            return False
        if not self.valid(node.right, val, upper):
            return False

        return True
