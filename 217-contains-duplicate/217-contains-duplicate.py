class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
       #IDEA1: pick each elt, and search. Run: O(n^2) Space: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] ==nums[j]: return True
        # return False
        
        #IDEA2: sort and see the adjacent elt : Run: O(nlogn+n) Space: O(1)
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]: return True
        # return False
        
        #IDEA3: create set and see if elt to be added already exist. O(n) run and space
        # numSet = set()
        # for num in nums:
        #     if num in numSet: return True
        #     numSet.add(num)
        # return False
    
        #same as IDEA3
        return len(set(nums)) != len(nums)  