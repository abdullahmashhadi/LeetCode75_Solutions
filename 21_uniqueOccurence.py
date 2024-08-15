from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict={}
        for num in arr:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]+=1
        occurences=list(dict.values())
        uniqueOccurences=set(occurences)
        return len(occurences)==len(uniqueOccurences)
nums1=list(map(int,input("Enter the space separated array of numbers :\n").split()))
sol=Solution()
output=sol.uniqueOccurrences(nums1)
print(output)
            
        
        