class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0, len(numbers)-1
        while i<j: # not <= because i and j has to be unique
            if numbers[i]+numbers[j] > target: j-=1
            elif numbers[i]+numbers[j] < target: i+=1
            else: return [i+1,j+1]
