class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix_sum=0
        res=0
        for i in range(0,len(gain)):
                prefix_sum+=gain[i]
                res=max(res,prefix_sum)
        return res

            
gain=list(map(int,input("Enter space-separated array:\n").split()))
sol=Solution()
output=sol.largestAltitude(gain)
print(output)