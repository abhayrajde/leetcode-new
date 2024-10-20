class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        def bs(isLeft):
            l = 0
            r = len(nums) - 1
            found = -1

            while l <= r:
                mid = (r + l) // 2

                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    found = mid
                    if isLeft: r = mid - 1
                    else: l = mid + 1
            return found
        
        return [bs(True), bs(False)]
