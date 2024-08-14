class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        
        return count
nums=list(map(int,input("Enter space-separated array:\n").split()))
k=int(input("Enter k-sum to check:\n"))
sol=Solution()
output=sol.maxOperations(nums,k)
print(output)