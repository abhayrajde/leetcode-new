class Solution(object):
    def minimumDeletions(self, s):
        a_count_right = [0 for _ in range(len(s))]
        for i in range(len(s)-2, -1, -1):
            a_count_right[i] = a_count_right[i+1]
            if(s[i+1] == "a"):
                a_count_right[i] += 1
        b_count_left = 0
        res = len(s)
        for i,ele in enumerate(s):
            res = min(res, a_count_right[i] + b_count_left)
            b_count_left += 1 if ele == "b" else 0
        return res
        """
        :type s: str
        :rtype: int
        """
        
