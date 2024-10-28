class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        
        def bs(left, right):
            while left <= right:
                mid = (left + right) // 2
                if target == nums[mid]:
                    return mid
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        found = bs(0, l-1)
        if found != -1: return found
        return bs(l, len(nums)-1)
