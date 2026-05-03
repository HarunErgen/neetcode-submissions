# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [(root, False)]

        while stack:
            cur, v = stack.pop()
            if cur:
                if v:
                    if self.is_leaf(cur.left) and cur.left.val == target:
                        cur.left = None
                    if self.is_leaf(cur.right) and cur.right.val == target:
                        cur.right = None
                else:
                    stack.append((cur, True))
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))

        if self.is_leaf(root) and root.val == target:
            return None

        return root
    
    def is_leaf(self, node):
        if not node: return False
        return node.right is None and node.left is None 