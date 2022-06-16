class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # #idea 1: sort and group. Runtime: O( s*nlogn), Space: O(s); s = len(strs), n = avg len of str in strs
        # arrToWord = defaultdict(list)
        # for i in range(len(strs)):
        #     arrToWord[ tuple(sorted(strs[i])) ].append( strs[i])
        # return arrToWord.values()                    
        
        #idea2: use arr of len(26) instead of sort. Runtime:O(s*n) Space: O(s)
        arrToWord = defaultdict(list)
        for word in strs: #for each word, create an arr of len 26 to encode a - z
            arr = [0]*26
            for c in word:
                arr[ord(c)-ord('a')] +=1
            
            arrToWord[ tuple(arr)].append(word) #create dict of arr -> list of words
                
        return arrToWord.values()

