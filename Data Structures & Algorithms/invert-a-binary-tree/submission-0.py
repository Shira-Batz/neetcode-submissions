# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        if root.left and root.right:
            temp = TreeNode(root.left.val, root.left.left, root.left.right)
            root.left = TreeNode(root.right.val, root.right.left, root.right.right)
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)

        elif root.left:
            root.right = TreeNode(root.left.val, root.left.left, root.left.right)
            root.left = None
            self.invertTree(root.right)

        elif root.right:
            root.left = TreeNode(root.right.val, root.right.left, root.right.right)
            root.right = None
            self.invertTree(root.left)
        return root
        