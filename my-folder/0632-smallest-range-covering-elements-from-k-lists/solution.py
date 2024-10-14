class Solution(object):
    def smallestRange(self, nums):
        k = len(nums)
        min1 = nums[0][0]
        max1 = nums[0][0]
        min_heap = []
        for i in range(k):
            min1 = min(min1, nums[i][0])
            max1 = max(max1, nums[i][0])
            heapq.heappush(min_heap, (nums[i][0], i, 0))      #item_val, item_list_index, item_index

        res = [min1, max1]
        while True:
            item_val,l_ind,ele_ind  = heapq.heappop(min_heap)
            ele_ind += 1
            if(ele_ind == len(nums[l_ind])):
                return res
            next_val = nums[l_ind][ele_ind]
            heapq.heappush(min_heap, (next_val, l_ind, ele_ind))
            min1 = min_heap[0][0]
            max1 = max(max1, next_val)

            if(max1 - min1 < res[1] - res[0]):
                res = [min1, max1]
            
        return res

        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
