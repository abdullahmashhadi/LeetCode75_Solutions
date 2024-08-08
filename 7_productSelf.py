# # Sol1 = O(n^2)
# class Solution:
#     def productSelf(self,nums:list)->list:
#         length=len(nums)
#         output=[1]*length
#         for i in range (length):
#             for j in range(length):
#                 if i!=j:
#                     output[i]=output[i]*nums[j]
#         return output

# nums=list(map(int,input("Write a space-separated array of numbers:\n").split()))
# sol=Solution()
# answer=sol.productSelf(nums)
# print(answer)

# # Sol2 =O(n) but with division operator
# class Solution:
#     def productSelf(self,nums:list)->list:
#         length=len(nums)
#         output=[0]*length
#         product=1
#         zeros=0
#         for i in range (length):
#             if(nums[i]!=0):
#                 product*=nums[i]
#             else:
#                 zeros+=1
#         if zeros>1:
#             return output
#         for i in range (length):
#             if (nums[i]==0):
#                 output[i]=product
#             elif zeros==0:
#                 output[i]=product//nums[i]
#             else:
#                 output[i]=0
            
#         return output
# nums=list(map(int,input("Write a space-separated array of numbers:\n").split()))
# sol=Solution()
# answer=sol.productSelf(nums)
# print(answer)

# #Sol3: O(n) without division operator but O(n) space complexity
# class Solution:
#     def productSelf(self,nums:list)->list:
#         length=len(nums)
#         output=[1]*length
#         prefix_product=[nums[0]]*length
#         postfix_product=[nums[length-1]]*length
#         for i in range(1,length):
#             prefix_product[i]=prefix_product[i-1]*nums[i]
#         for i in range(length-2,-1,-1):
#             postfix_product[i]=postfix_product[i+1]*nums[i]
#         for i in range(length):
#             if i==0:
#                 output[i]=postfix_product[i+1]
#             elif i==length-1:
#                 output[i]=prefix_product[i-1]
#             else:
#                 output[i]=prefix_product[i-1]*postfix_product[i+1]
#         return output

            
# nums=list(map(int,input("Enter your array (space-separated:)\n").split()))   
# sol=Solution()
# answer=sol.productSelf(nums)
# print(answer)

#Sol4: O(n) without division operator O(1) space complexity
class Solution:
    def productSelf(self,nums:list)->list:
        output=[1]*len(nums)
        prefix=1
        postfix=1
        for i in range(0,len(nums)):
            output[i]=prefix
            prefix*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            output[i]*=postfix
            postfix*=nums[i]
        return output

nums=list(map(int,input("Enter your array (space-separated:)\n").split()))   
sol=Solution()
answer=sol.productSelf(nums)
print(answer)