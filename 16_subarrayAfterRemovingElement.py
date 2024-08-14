class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        num_zeros=0
        l=0
        max_w=0
        for r in range(len(nums)):
            if (nums[r]==0):
                num_zeros+=1
            while num_zeros>1:
                if nums[l]==0:
                    num_zeros-=1
                l+=1
            w=r-l+1
            max_w=max(max_w,w)
        return max_w-1
nums=list(map(int,input("Enter space separated array of 0s and 1s:\n").split()))
sol=Solution()
output=sol.longestSubarray(nums)
print(f"max numbers of consecutive 1s subarray after deleting one 0 is: {output}")       
        