class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = len(flowerbed)
        new_flowerbed = flowerbed[:]
        plot = [None] * length
        if n == 0:
            return True
        for i in range(length):
            if i == 0:
                if length == 1:
                    plot[i] = new_flowerbed[i] == 0
                else:
                    plot[i] = new_flowerbed[i] == 0 and new_flowerbed[i+1] == 0
            elif i == length - 1:
                plot[i] = new_flowerbed[i] == 0 and new_flowerbed[i-1] == 0
            else:
                plot[i] = new_flowerbed[i] == 0 and new_flowerbed[i-1] == 0 and new_flowerbed[i+1] == 0
        for i in range(length):
            if plot[i] is True:
                new_flowerbed[i] = 1
                n -= 1
                if i > 0:
                    plot[i-1] = False
                if i < length - 1:
                    plot[i+1] = False
                if n == 0:
                    return True,new_flowerbed
        return n <= 0,new_flowerbed
flowerbed=list(map(int,input("Enter space-separated array of flowerbed:\n").split()))
n=int(input("Enter the number of flowers to pot:\n"))

sol=Solution()
answer,plottedFlowerBed=sol.canPlaceFlowers(flowerbed,n)
if (answer==True):
    print(f"Yes, you can plot {n} flowers in the flowerbed:\n {flowerbed} as:\n {plottedFlowerBed}")
else:
    print(f"No, you cannot plot {n} flowers in the flowerbed:\n {flowerbed}")

                
        

        