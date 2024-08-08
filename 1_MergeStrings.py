
def mergeStrings(word1:str,word2:str)->str:
    len1=len(word1)
    len2=len(word2)
    merged=""
    if(len1>len2):
                for i in range(len2):
                    merged+=word1[i]
                    merged+=word2[i]
                for i in range (len2,len1):
                    merged+=word1[i]
    elif (len2>len1):
                for i in range(len1):
                    merged+=word1[i]
                    merged+=word2[i]
                for i in range (len1,len2):
                    merged+=word2[i]
    else:
                for i in range(len1):
                    merged+=word1[i]
                    merged+=word2[i]
    return merged
word1=input("Enter 1st string:\n")
word2=input("Enter 2nd string:\n")
merged=mergeStrings(word1,word2)
print("The merged string is: "+merged)
