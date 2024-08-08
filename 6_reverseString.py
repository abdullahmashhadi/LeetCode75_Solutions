class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip().split()
        s_list=list(s[::-1])
        length=len(s_list)
        reverse_string=[]
        for index,word in enumerate(s_list):
            reverse_string.append(word)
            if(index!=length-1):
                reverse_string.append(' ')
        return ''.join(reverse_string)
s=input("Enter string:\n")
sol=Solution()
answer=sol.reverseWords(s)
print(answer)