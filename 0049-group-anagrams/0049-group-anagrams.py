class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #O(len(strs)*num of char log num of char), space: len*strs: sort and hash
            
        # len(strs)*number of char time, space:len(strs) 
        dictAna = defaultdict(list)
        for elt in strs:
            arr = [0]*26
            for e in elt:
                arr[ord (e)-ord('a')] +=1
            dictAna[tuple(arr)].append(elt)
            
        result = []    
        for k,v in dictAna.items():
            result.append(v)
        return result