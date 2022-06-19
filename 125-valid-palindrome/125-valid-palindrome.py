class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #idea1: build a string using extra memory and check if reverse string == string. 
        #Runtime: O(n) Space: O(n)
        
        #idea2: use two pointer Runtime: O(n)
        
        if len(s) ==0 or len(s)==1: return True
        
        s= s.lower()
        i,j = 0, len(s)-1
        while i<j:
            while i <j and s[i].isalnum() == False:
                i+=1
            while i <j and s[j].isalnum() == False:
                j-=1
            if s[i] != s[j]: return False
            i+=1
            j-=1
        return True