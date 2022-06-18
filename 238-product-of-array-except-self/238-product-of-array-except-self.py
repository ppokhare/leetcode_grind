class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #idea 0: if division was permited. This is still wrong; take care of divide by 0
#         product = 1
#         for num in nums: product *= num
#         return [product/num for num in nums]
    
    
        #idea 1: use pre and post product and result is pre*post         
#         pre = [1]*len(nums)
#         for i in range(1,len(nums)):
#             pre[i] = pre[i-1]*nums[i-1]
        
#         post = [1]*len(nums)
#         for i in range(len(nums)-2, -1, -1):
#             post[i] = post[i+1]*nums[i+1]
        
#         print(pre,post)
#         return [x*y for x,y in zip(pre,post)]
    
    
        #idea2: same as 1 but time efficient 
        pre = [1]*len(nums)
        for i in range(1,len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
        
        post = 1
        for i in range(len(nums)-2, -1, -1):
            post*=nums[i+1]
            pre[i] *=post
                
        return pre