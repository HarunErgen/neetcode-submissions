# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        queue = deque(preorder)

        def build(inorder):
            if not inorder:
                return
            if len(inorder) == 1:
                return TreeNode(queue.popleft())
            
            root = TreeNode(queue.popleft())
            root.left = build(inorder[:inorder.index(root.val)])
            root.right = build(inorder[inorder.index(root.val)+1:])
            
            return root
        
        root = None
        
        return build(inorder)