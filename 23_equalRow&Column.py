from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        totalPairs=0
        n=len(grid)
        for i in range(n):
            for j in range(n):
                count=0
                for k in range (n):
                    if grid[i][k]==grid[k][j]:
                        count+=1
                    else:
                        break
                if count==n:
                    totalPairs+=1
        return totalPairs
n=int(input("Enter the size of your nxn matrix (enter n)\n"))
grid=[0]*n
for i in range(n):
    grid[i]=list(map(int,input(f"Enter space separated {i+1}th array\n").split()))
sol=Solution()
output=sol.equalPairs(grid)
print(f"Total row-column pairs are: {output}")
