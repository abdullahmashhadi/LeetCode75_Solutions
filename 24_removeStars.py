class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for char in s:
            if char!='*':
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)
string=input("Enter string:\n")
sol=Solution()
output=sol.removeStars(string)
print(f"String {string} after operations is: {output}")