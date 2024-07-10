class Solution(object):
    def minOperations(self, logs):
        count = 0 
        for i in range(len(logs)):
            temp = logs[i].split("/")
            if temp[0] == "..":
                if count != 0:
                    count -= 1
            elif temp[0] == ".":
                continue
            else:
                count += 1
        return count
        """
        :type logs: List[str]
        :rtype: int
        """
        
