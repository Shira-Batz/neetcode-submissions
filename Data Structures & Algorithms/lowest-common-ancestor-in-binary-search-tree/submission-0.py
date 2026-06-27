# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        rv, pv, qv = root.val, p.val, q.val
        lca = root
        if pv > rv and qv > rv:
            lca = self.lowestCommonAncestor(root.right, p, q)
        elif pv < rv and qv < rv:
            lca = self.lowestCommonAncestor(root.left, p, q)
        return lca
        
        