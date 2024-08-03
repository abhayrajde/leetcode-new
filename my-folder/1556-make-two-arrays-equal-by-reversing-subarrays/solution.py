class Solution(object):
    def canBeEqual(self, target, arr):
        arr_map = defaultdict(int)
        target_map = defaultdict(int)
        for i in range(len(arr)):
            arr_map[arr[i]] += 1
            target_map[target[i]] += 1
        
        for key, value in arr_map.items():
            if target_map[key] != value:
                return False
        return True
                

        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        
