from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        list1 = []
        list2 = []
        for n in set1:
            if n not in set2:
                list1.append(n)
        for n in set2:
            if n not in set1:
                list2.append(n) 
        return [list1, list2]   
nums1=list(map(int,input("Enter the 1st space separated array of numbers :\n").split()))
nums2=list(map(int,input("Enter the 2nd space separated array of numbers :\n").split()))
sol=Solution()
output=sol.findDifference(nums1,nums2)
print(output)
