class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        i,j = 0, len(s)-1

        while i<=j:
            if s[i].isalnum() ==False: i+=1
            elif s[j].isalnum() ==False: j-=1
            elif s[i].lower() != s[j].lower(): return False
            else:
                i+=1
                j-=1
        return True