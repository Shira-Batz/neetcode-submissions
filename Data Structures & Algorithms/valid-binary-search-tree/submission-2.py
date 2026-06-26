# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        arr = inorder(root)
        sort_arr = arr.copy()
        sort_arr = list(set(sort_arr))
        sort_arr.sort()
        print(arr, "  ", sort_arr)
        return sort_arr == arr
