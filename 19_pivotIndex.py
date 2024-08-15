class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        totalSum=sum(nums)
        leftSum=0
        for i in range(len(nums)):
            rightSum=totalSum-leftSum-nums[i]
            if leftSum==rightSum:
                return i
            else:
                leftSum+=nums[i]
        return -1
nums=list(map(int,input("Enter the space separated array of numbers :\n").split()))
sol=Solution()
output=sol.pivotIndex(nums)
print(f"The pivot index is {output}")