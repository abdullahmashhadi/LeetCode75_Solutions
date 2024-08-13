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