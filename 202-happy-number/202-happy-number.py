class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #1. get individual digits
        #2. compute the square 
        #if 1: True 
        #else: check if exists in seenSet: if so return False if not go to #1 and add to set
        
        seenSet= set()
        while True:
            n = str(n)
            sum = 0
            for i in range(len(n)):
                sum+=int(n[i])**2

            if sum == 1: return True
            else:
                if sum in seenSet:
                    return False
                else:
                    seenSet.add(sum)
                    n = sum