class Solution(object):
    def permute(self, nums): 
        res = []
        
        def backtrack(ind,nums):
            if(ind == len(nums)):
                res.append(nums[:])
                return
            
            for i in range(ind,len(nums)):
                nums[ind],nums[i] = nums[i],nums[ind]
                backtrack(ind+1,nums)
                nums[ind],nums[i] = nums[i],nums[ind]
        backtrack(0,nums)
        return res
                
        
        #Space Complexity  - O(N!) * N
#         res = []
#         freq = [0]*len(nums)
#         curr = []
#         def backtrack(nums,curr,res,freq):
#             if (len(curr) == len(nums)):
#                 res.append(curr[:])
#                 return
            
#             for i in range(len(nums)):
#                 if(freq[i] == 0):
#                     freq[i] = 1
#                     curr.append(nums[i])
#                     backtrack(nums,curr,res,freq)
#                     curr.pop()
#                     freq[i] = 0
#         backtrack(nums,curr,res,freq)
#         return res
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
