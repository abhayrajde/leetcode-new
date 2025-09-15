class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This code can handle 5sum, 6sum, ....so on
        nums.sort()
        res, curr = [], []
        
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    curr.append(nums[i])
                    kSum(k-1, i+1, target - nums[i])
                    curr.pop()
                return

            # Two Pointer - Two Sum
            l, r = start, len(nums) - 1
            while l < r:
                tsum = nums[l] + nums[r]
                if tsum < target:
                    l += 1
                elif tsum > target:
                    r -= 1
                else:
                    res.append(curr + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        kSum(4,0,target)
        return res


        # Below code is not scalable code
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                # Two Pointer - Two Sum
                l, r = j + 1, len(nums) - 1
                while l < r:
                    fsum = nums[i] + nums[j] + nums[l] + nums[r]
                    if fsum < target:
                        l += 1
                    elif fsum > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and l > j+1 and nums[l] == nums[l-1]:
                            l += 1
        return res
