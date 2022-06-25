class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # idea1: find all subtring; check if they have unique char and return longest lenght
        
        #idea2: sliding the window: Runtime: O(n) Space: O(n)
        seen = set()
        i,j = 0,0
        maxResult = 0
        while j <len(s):
            if s[j] not in seen: # add elt in the set and side j
                seen.add(s[j])
                maxResult = max(maxResult, j-i+1)
                j +=1
            else: # slide i you get rid of the duplicate one
                while s[j] in seen:
                    seen.remove(s[i])
                    i+=1
                seen.add(s[j])
                j+=1
        return maxResult