class Solution(object):
    def nextPermutation(self, nums):
        # if the length is 2 or less then 2 then we just need to reverse the number
        if(len(nums)<=2):
            return nums.reverse()
        # STEP 1    from the last term traversing right to left and finding the downfall, ie 
        # for eg: nums = [4,5,3,2,1] so 2>1, 3>2, 5>3, buttt 4!>5 ..now this is downfall
        i = len(nums)-1
        while(i>0 and nums[i] <= nums[i-1]):
            i-=1
        
        # if we didnt found the downfall then reverse the whole string
        if(i == 0):
            return (nums.reverse())
            
        # STEP 2 : once we find the element with downfall, we need to find the no. just large than that element and swap the no.with that just large no.
        for j in range(len(nums)-1,i-1,-1):
            if(nums[j] > nums[i-1]):
                nums[j],nums[i-1] = nums[i-1],nums[j]
                break
        # STEP 3 : now just sort the nos. just after the number which is swapped
        nums[i:] = reversed(nums[i:])
        return nums
            
        
        """
        for i in range(len(nums)-1,0,-1):
            if(nums[i]>nums[i-1]):
                nums[i],nums[i-1] = nums[i-1],nums[i]
                break
        else:
            nums.sort()
        """
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
