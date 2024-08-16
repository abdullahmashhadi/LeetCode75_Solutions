class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]
        for asteroid in asteroids:
            while stack and stack[-1]>0 and asteroid<0:
                if abs(asteroid)>stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid)==stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack
asteroids=list(map(int,input("Enter the asteroids (space-separated):\n").split()))
sol=Solution()
output=sol.asteroidCollision(asteroids)
print(f"Initial Asteroids: {asteroids}")
print(f"Asteroids after collision: {output}")