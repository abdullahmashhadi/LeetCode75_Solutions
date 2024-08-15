class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1)!=len(word2)):
            return False
        dict1={}
        dict2={}
        for char in word1:
            if char not in dict1:
                dict1[char]=1
            else:
                dict1[char]+=1
        for char in word2:
            if char not in dict2:
                dict2[char]=1
            else:
                dict2[char]+=1
        dict1Set=set(list(dict1.keys()))
        dict2Set=set(list(dict2.keys()))
        if (dict1Set!=dict2Set):
            return False
        frequency1=sorted(list(dict1.values()))
        frequency2=sorted(list(dict2.values()))
        if (frequency1!=frequency2):
            return False
        return True
word1=input("Enter 1st string:\n")
word2=input("Enter 2nd string:\n")
sol=Solution()
output=sol.closeStrings(word1,word2)
print(output)