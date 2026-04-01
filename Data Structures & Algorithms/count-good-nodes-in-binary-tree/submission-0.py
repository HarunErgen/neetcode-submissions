# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        stack = [(root, None)]
        count = 0

        while stack:
            node, p_max = stack.pop()
            if not p_max or node.val >= p_max:
                count += 1

            p_max = node.val if not p_max else max(node.val, p_max)

            if node.left:
                stack.append((node.left, p_max))
            if node.right:
                stack.append((node.right, p_max))

        return count





