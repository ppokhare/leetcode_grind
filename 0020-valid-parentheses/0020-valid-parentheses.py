class Solution:
    def isValid(self, s: str) -> bool:
        
        validP = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        p_stack= []
        for elt in s:
            if elt not in validP: p_stack.append(elt)       
            else:
                top_elt= p_stack.pop() if p_stack else " "
                if top_elt !=  validP[elt]: return False
        return len(p_stack) == 0