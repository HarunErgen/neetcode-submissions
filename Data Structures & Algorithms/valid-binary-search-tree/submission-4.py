# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        queue = deque([(root, None, None)])

        while queue:
            node, left_parent, right_parent = queue.popleft()
            node_val = node.val
            left_val = left_parent.val if left_parent else None
            right_val = right_parent.val if right_parent else None
            print(node_val, left_val, right_val)

            if node.left:
                if (not node.left.val < node.val) or (left_parent and node.left.val <= left_parent.val):
                    return False
                queue.append((node.left, left_parent, node))
            if node.right:
                if not node.right.val > node.val or (right_parent and node.right.val >= right_parent.val):
                    return False
                queue.append((node.right, node, right_parent))
        
        return True
