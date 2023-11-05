# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        # BRUTEFORCE solution to dfs root and for every node check for same Tree condition. O(root*subRoot)
        if not root and not subRoot: return True
        def isSameTree( p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
            #########recursive solution
            if not p and not q: return True
            if (p and not q) or (not p and q): return False  

            if p.val !=q.val: return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        
        
        stack = [root]
        while stack:
            node = stack.pop()
            if isSameTree(node, subRoot): return True
                
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False            