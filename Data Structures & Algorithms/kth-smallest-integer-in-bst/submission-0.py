# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def intraversal(node, count):
            if not node:
                return node, count
            if not node.left and not node.right:
                return node, count + 1

            left_node, left_count = intraversal(node.left, count)
            if left_count == k:
                return left_node, left_count
            if left_count == k - 1:
                return node, left_count+1
            right_node, right_count = intraversal(node.right, left_count + 1)
            if right_count == k:
                return right_node, right_count

            return node, right_count
        
        result_node, _ = intraversal(root, 0)
        return result_node.val
