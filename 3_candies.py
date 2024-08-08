class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        length=len(candies)
        result=[None]*length
        for i in range(length):
            for j in range(length):
                if(candies[i]+extraCandies<candies[j]):
                    result[i]=False
                    break
                else:
                    result[i]=True
        return result
candies= list(map(int, input("Enter space-separated integers: ").split()))
print("Array:", candies)
extra_candies=int(input("Enter the extra candies:\n"))
sol=Solution()
answer=sol.kidsWithCandies(candies,extra_candies)
print(answer)
        