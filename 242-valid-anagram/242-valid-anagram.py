class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #idea1: for each char in s find sam char in t and cross that off. Runtime: O(N^2) Space: O(1)
        
        
        #idea2: create two hashtable and comapre both are true. Runtume: O(n+n+n) Space: O(N+N)
        
        #idea 3: instead of two table create one. +1 for s and -1 for t and check if all value is 0. Runtime:O(n+n) Space: (n)
        
        if len(s) != len(t): return False #edge case
        
        anaDict = defaultdict(int)
        for i in range(len(s)):
            anaDict[s[i]] +=1
            anaDict[t[i]] -=1
        
        for _,v in anaDict.items():
            if v != 0: return False
        return True
            