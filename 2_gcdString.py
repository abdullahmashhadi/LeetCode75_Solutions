class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1=len(str1)
        len2=len(str2)
        s_divides_t=None
        x=""
        if(len1>len2):
            for i in range(len1):
                if(str1[i]!=str2[i%(len2)]):
                    s_divides_t=False
                else:
                    s_divides_t=True
        elif(len2>len1):
            for i in range(len2):
                if(str2[i]!=str1[i%(len1)]):
                    s_divides_t=False
                else:
                    s_divides_t=True
        else:
            for i in range(len1):
                if(str1[i]!=str2[i]):
                    s_divides_t=False
                else:
                    s_divides_t=True
        if (s_divides_t==True):
            if(len1>len2):
                for i in range(len2): 
                    if str2[i] not in x:
                        x+=str2[i]
                    
            elif(len2>len1):
                for i in range(len1):
                    if str1[i] not in x:
                        x+=str1[i]
            else:
                for i in range(len1):   
                    if str1[i] not in x:
                        x+=str1[i]
        return x

        