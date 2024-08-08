import sys
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums)<3:
            return False
        nums_i=sys.maxsize
        nums_j=sys.maxsize
        for num in nums:
            if num<= nums_i:
                nums_i=num
            elif num<= nums_j:
                nums_j=num
            else:
                return True
        return False
nums=list(map(int,input("Enter space separated array:\n").split()))
sol=Solution()
output=sol.increasingTriplet(nums)
print(output)