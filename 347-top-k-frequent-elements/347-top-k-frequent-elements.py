class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
#         idea1: counter and sort it and take first k unique values: Runtime: O(nlogn) spaceL O(n)
#         count = Counter(nums) #create a dict of unique elt in nums and its # of appearance. 
#         result = [keys for keys, values in sorted(count.items(), key=lambda x: x[1])] # sort dict by values and save the keys in result
#         return result[-k:] # result is the lask k values
        
    
#         #idea2: counter and heap: runtime: O(klogn) space: O(n)
#         count = Counter(nums)
#         heap = []
#         for keys,values in count.items():
#             heapq.heappush(heap, (-values, keys))

#         result =[]
#         for i in range(k):
#             result.append(heapq.heappop(heap)[1])
#         return result
            
        
        #idea3: use counter,and bucketsort. runtime: O(n) space: O(n)
        count = Counter(nums)
        arr = [[] for i in range(len(nums))]
       
        for key,value in count.items(): #if 1 apperes 3 times then in thrid idex of arr write 1.
            arr[value-1].append(key)    
        
        result = []
        for i in range(len(arr)-1, -1, -1):#loop thru arr in decending order and fill result array
            for n in arr[i]:
                result.append(n)
                if len(result) ==k:
                    return result
           