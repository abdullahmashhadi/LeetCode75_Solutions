class Solution:
    def reverseVowels(self, s: str) -> str:
        new_str=""
        vowels=["a","e","i","o","u","A","E","I","O","U"] 
        for char in s:
            if char in vowels:
                new_str+=char
        new_str=new_str[::-1]
        str_list=list(s)
        i=0
        for index,char in list(enumerate(str_list)):
            if char in vowels:
                str_list[index]=new_str[i]
                i=i+1
        result_str=''.join(str_list)
        return result_str
s=input("Enter the string:\n")
sol=Solution()
answer=sol.reverseVowels(s)
print(answer)


# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         v=["a","e","i","o","u","A","E","I","O","U"] 
#         l=0
#         r=len(s)-1
#         s=list(s)
#         while(l<r):
#             if s[l] in v and s[r] in v:
#                 s[l],s[r]=s[r],s[l]
#                 l+=1
#                 r-=1
#             if s[l] not in v:
#                 l+=1
#             if s[r] not in v:
#                 r-=1
#         return ''.join(s)