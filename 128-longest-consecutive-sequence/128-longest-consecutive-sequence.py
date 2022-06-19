class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #idea 0:if sorting was allowed: 
        #sort and check for nums[i]+1 == nums[i+1]. keep track of lengest sequence
        
        #idea1: using set to check if num+1 in nums or not in O(1)
        #runtime: O(n) Space: O(n)
        if len(nums) == 0: return 0 
        numSet = set(nums)
        maxSeq = 1
        for num in nums:
            seq = 1
            if num-1 not in numSet: # check if num is the start of seq
                while num+1 in numSet:
                    seq+=1
                    num+=1
            maxSeq = max(maxSeq,seq)
        return maxSeq