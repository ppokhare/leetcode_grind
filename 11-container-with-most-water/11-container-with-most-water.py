class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #idea 0: be greedy: pick two largest elt
        # it doesnot always work: for ex: [1,1,2,3,1,1,1]; true result is 6 but this way gives 2 instead.
        
        #idea1: be greedy but in horizontal axis. Runtime: O(n)
        l,r = 0, len(height)-1 #the max in the horizontal axis is if you pick first and last elt. 
        maxArea = 0
        while l < r:
            area = (r-l)*min(height[l],height[r])
            maxArea = max(area, maxArea)
            
            #move pointer which is more favorable. BE GREDDY!!
            if height[l] < height[r]:l+=1
            else: r-=1
        return maxArea