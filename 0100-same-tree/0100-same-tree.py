# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if (p and not q) or (not p and q): return False
        
        stack = [(p,q)]
        
        while stack:
            p_node, q_node = stack.pop()
            
            if p_node.val !=   q_node.val: return False
            
            if p_node.left and q_node.left: stack.append((p_node.left, q_node.left))
            elif  not p_node.left and  not q_node.left: pass
            else: return 
            
            if p_node.right and q_node.right: stack.append((p_node.right, q_node.right))
            elif  not p_node.right and  not q_node.right: pass
            else: return False
            
        
        return True
            
        