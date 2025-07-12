class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([t, i])
        return res
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
