class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        totalSum=sum(nums[:k])
        maxSum=totalSum
        for i in range(k,len(nums)):
            totalSum-=nums[i-k]
            totalSum+=nums[i]
            maxSum=max(maxSum,totalSum)

        return maxSum/k

nums=list(map(int,input("Enter space-separated array:\n").split()))
k=int(input("Enter the length of subarray to check:\n"))
sol=Solution()
output=sol.findMaxAverage(nums,k)
print(f"max average of length {k} subarray is: {output}")
