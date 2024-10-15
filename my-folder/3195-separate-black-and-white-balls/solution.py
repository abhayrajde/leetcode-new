class Solution(object):
    def minimumSteps(self, s):
        lst = list(s)
        steps = 0
        i = 0
        while(i < len(lst) and lst[i] == "0"):
            i += 1
        j = i + 1
        while(j < len(lst)):
            if lst[j] == "1":
                j += 1
            else:
                steps += (j - i)
                j += 1
                i += 1
        return steps

        """
        :type s: str
        :rtype: int
        """
        
