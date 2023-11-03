# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #preorder DFS iteratively
        if not root: return 0
        stack = [(root,1)]
        res = 1
        while stack:
            node, depth = stack.pop()
            if node.left:
                stack.append((node.left,depth+1))
            if node.right:
                stack.append((node.right,depth+1))
            res = max(res, depth)
        return res
    
        
#         # DFS recursively
#         if not root: return 0 # if empty
#         return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    
#         #BFS
#         if not root: return 0    
#         traverse = deque() # init queue
#         traverse.append(root)# put root in queue
#         level = 0
        
#         while traverse: # while queue is not empty
#             for i in range(len(traverse)): #go thur each elt in queue, remove it and put its children
#                 node = traverse.popleft()
#                 if node.left: traverse.append(node.left)
#                 if node.right: traverse.append(node.right)
#             level +=1
#         return  level
        