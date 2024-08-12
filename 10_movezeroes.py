class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        while(r<len(nums)):
            if nums[r]==0:
                r+=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r+=1

nums=list(map(int,input("Enter your array (space-separated):\n").split()))
sol=Solution()
sol.moveZeroes(nums)
print(nums)