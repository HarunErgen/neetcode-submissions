# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        prev = None

        left = False

        while cur:
            prev = cur
            if val > cur.val:
                cur = cur.right
                left = False
            else:
                cur = cur.left
                left = True

        if not prev:
            return TreeNode(val)

        if left:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
        
        return root
