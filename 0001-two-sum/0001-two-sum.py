class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         # n^2 time, 1 space: loop twice and match to the  target
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]+nums[j] == target: return [i,j]
                
        # n time, n space: use a hashtable to keep track of what you have seen before 
    
        twoSumDict = defaultdict(int)
        for i,n in enumerate(nums):
            if target -n in twoSumDict: 
                return [i, twoSumDict[target-n]]
            twoSumDict[n]= i