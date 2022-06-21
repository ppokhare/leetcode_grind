class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
#         #idea0: triple loop; !beware of duplicates. 
#         result =[]
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         result.append([nums[i], nums[j], nums[k]])
#         return result
    
#         #diea1: double loop. keep one elt fixed and do two sum. Still duplicate problem
#         for i in range(len(nums)):
#             target = -nums[i]
#             numSet = set()
#             for j in range(len(nums)):
#                 if j ==i: continue
#                 if nums[j]-target in numSet: result.append([nums[i], nums[j], numSet[nums[j]]])
#                 else: numSet.add(nums[j])
#         return result
    
        #idea2:#sort it + one elt fixed and two sum II    Runtime: O(n^2)
        nums.sort() 
        result = []
        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]: continue # prevent duplicate
            
            l,r = i+1, len(nums)-1
            while l<r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0: r-=1
                elif threeSum < 0: l+=1
                else: 
                    result.append([nums[i], nums[l], nums[r]]) 
                    l+=1
                    r-=1
                    while l <r and nums[l] == nums[l-1]: l+=1
                    while l<r and nums[r] == nums[r+1]:  r-=1
                    
        return result