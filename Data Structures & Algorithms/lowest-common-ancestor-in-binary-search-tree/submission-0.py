# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p == q: return p

        def dfs(start):
            if not start: return
            if start.val == p.val or start.val == q.val:
                return start
            
            left = dfs(start.left)
            right = dfs(start.right)
            if left and right:
                return start
            
            return left or right
        
        return dfs(root)

