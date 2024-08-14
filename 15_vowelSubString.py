class Solution:
    def isVowel(self, char:str)-> int:
        vowels=['a','e','i','o','u']
        if char in vowels:
            return 1
        else:
            return 0
    def maxVowels(self, s: str, k: int) -> int:
        Vowels=0
        for char in s[:k]:
            if self.isVowel(char):
                Vowels+=1
        maximumVowels=Vowels
        for i in range(k,len(s)):
            Vowels-=self.isVowel(s[i-k])
            Vowels+=self.isVowel(s[i])
            maximumVowels=max(maximumVowels,Vowels)
        return maximumVowels
s=input("Enter string:\n")
k=int(input("Enter the length of subarray to check:\n"))
sol=Solution()
output=sol.maxVowels(s,k)
print(f"max numbers of vowels in length {k} subarray is: {output}")

# class Solution:
#     def isVowel(self, char:str)-> int:
#         vowels={'a':1,'e':1,'i':1,'o':1,'u':1}
#         return vowels.get(char)
#     def maxVowels(self, s: str, k: int) -> int:
#         l,r,max_,current=0,0,0,0
#         while r<len(s):
#             if self.isVowel(s[r]): current +=1
#             if(r-l+1>k):
#                 if(self.isVowel(s[l])): current-=1
#                 l+=1
            
#             max_=max(current,max_)
#             r+=1
#         return max_