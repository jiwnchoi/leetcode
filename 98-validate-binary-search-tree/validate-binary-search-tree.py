# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], gt=-float('inf'), lt=float('inf')) -> bool:
        if not root:
            return True
            
        if not (gt < root.val < lt):
            return False
            
        return self.isValidBST(root.left, gt, root.val) and \
               self.isValidBST(root.right, root.val, lt)