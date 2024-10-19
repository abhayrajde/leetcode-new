class Solution(object):
    def maxTurbulenceSize(self, arr):
        left, right = 0, 1
        prev_sign = ""
        max_size = 1
        while right < len(arr):
            if arr[right - 1] > arr[right] and prev_sign != ">":
                prev_sign = ">"
                max_size = max(max_size, right - left + 1)
                right += 1
            
            elif arr[right - 1] < arr[right] and prev_sign != "<":
                prev_sign = "<"
                max_size = max(max_size, right - left + 1)
                right += 1
            
            else:
                prev_sign = ""
                right = right + 1 if arr[right] == arr[right - 1] else right
                left = right - 1
        return max_size

        """
        :type arr: List[int]
        :rtype: int
        """
        
