# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         len1=len(str1)
#         len2=len(str2)
#         s_divides_t=None
#         x=""
#         if(len1>len2):
#             for i in range(len1):
#                 if(str1[i]!=str2[i%(len2)]):
#                     s_divides_t=False
#                 else:
#                     s_divides_t=True
#         elif(len2>len1):
#             for i in range(len2):
#                 if(str2[i]!=str1[i%(len1)]):
#                     s_divides_t=False
#                 else:
#                     s_divides_t=True
#         else:
#             for i in range(len1):
#                 if(str1[i]!=str2[i]):
#                     s_divides_t=False
#                 else:
#                     s_divides_t=True
#         if (s_divides_t==True):
#             if(len1>len2):
#                 for i in range(len2): 
#                     if str2[i] not in x:
#                         x+=str2[i]
                    
#             elif(len2>len1):
#                 for i in range(len1):
#                     if str1[i] not in x:
#                         x+=str1[i]
#             else:
#                 for i in range(len1):   
#                     if str1[i] not in x:
#                         x+=str1[i]
#         return x

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smaller=str2 if len(str2)<len(str1) else str1
        larger=str1 if len(str1)>len(str2) else str2
        gcd_string=""
        for i in range (len(smaller)):
            prefix=smaller[0:i+1]
            if prefix*int((len(larger)/len(prefix)))==larger and prefix*int((len(smaller)/len(prefix)))==smaller:
                    gcd_string=prefix
        return gcd_string

        
        

        
        