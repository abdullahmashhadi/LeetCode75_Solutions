class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=0
        max_w=0
        num_zeros=0
        for r in range(len(nums)):
            if nums[r]==0:
                num_zeros+=1
            while num_zeros>k:
                if nums[l]==0:
                    num_zeros-=1
                l+=1
            w=r-l+1
            max_w=max(max_w,w)
        return max_w
nums=list(map(int,input("Enter space separated array of 0s and 1s:\n").split()))
k=int(input("Enter the number of 0s to flip:\n"))
sol=Solution()
output=sol.longestOnes(nums,k)
print(f"max numbers of consecutive 1s subarray is: {output}")      



        