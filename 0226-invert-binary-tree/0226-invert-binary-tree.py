# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
#         if not root: return root
#         stack = [root]
#         while stack:
#             node = stack.pop()
            
#             if node.left:  stack.append(node.left)
#             if node.right:stack.append(node.right)
            
#             l = node.left
#             node.left = node.right
#             node.right = l
                
#         return root
    
    
    
        #recursiverly
        if not root: return None
        
        #swap the child
        left = root.left
        root.left = root.right
        root.right = left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root