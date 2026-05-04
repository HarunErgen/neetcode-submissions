# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(n):
            if n is None:
                return 0, 0
            
            left_res, right_res = dfs(n.left), dfs(n.right)

            with_root = n.val + left_res[1] + right_res[1]
            without_root = max(left_res) + max(right_res)

            return with_root, without_root
        
        return max(dfs(root))
