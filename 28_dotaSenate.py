from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate=list(senate)
        radiant=deque()
        dire=deque()
        for i in range(len(senate)):
            if senate[i]=="R":
                radiant.append(i)
            else:
                dire.append(i)
        while(dire and radiant):
            d=dire.popleft()
            r=radiant.popleft()
            if r<d:
                radiant.append(r+len(senate))
            else:
                dire.append(d+len(senate))
        return "Radiant" if not dire else "Dire"
senate=input("Enter string representing members of senate(R/D only):\n")
sol=Solution()
output=sol.predictPartyVictory(senate)
print(output)