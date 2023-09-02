from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # n^2 time, 1 space: looping s and find s[i] in t and crossing it off nad at the check if t is empty
        # nlog n time, 1 space: short and check if they are same: sorted(s) ==sorted(t)

        # n time, n space: create dict and +1 for s and -1 for t and check if all value is 0. 
        if (len(s) != len(t)): return False
        anagram = defaultdict(int)
        for i in range(len(s)):
            anagram[s[i]]+=1
            anagram[t[i]]-=1
        
        for k,v in anagram.items():
            if v !=0: return False
        return True


 