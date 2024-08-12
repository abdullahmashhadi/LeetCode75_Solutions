class Solution:
    def compress(self, chars: list[str]) -> int:
        s=[]
        i=0
        while(i<len(chars)):
            char=chars[i]
            count=0
            while (i<len(chars) and chars[i]==char):
                count+=1
                i+=1
            s.append(char)
            if (count>1):
                s.extend(list(str(count)))
        chars[:len(s)]=s
        return len(s)
chars=list(map(str,input("Enter space separated string (like a a b b c c c)\n").split()))
sol=Solution()
output1=sol.compress(chars)
output2=chars[:output1]
print(f"Length of compressed string is: {output1}")
print(f"The new char array is:\n {output2}")