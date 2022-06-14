class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #idea1: loop twice and check if nums[i]+nums[j] == target Runtime: O(n^2) Space: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if target - nums[i] == nums[j]: return [i,j]
        
        #idea2: use hashmap to keep track of what you have seen. Runtime: O(n) space: O(n)
        twoSum = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in twoSum: return [i,twoSum[nums[i]]]
            twoSum[target-nums[i]] = i
        