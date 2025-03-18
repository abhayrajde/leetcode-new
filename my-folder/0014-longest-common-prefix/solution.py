class Solution(object):
    def longestCommonPrefix(self, strs):
        strLengthList = []
        for i in range(len(strs)):
            strLengthList.append((len(strs[i]), i))
        strLengthList = sorted(strLengthList, key = lambda x: x[0])
        element = strs[strLengthList[0][1]]
        result = ""
        for i in range(len(element)):
            for j in range(len(strs)):
                if strs[j][i] != element[i]:
                    return result
            result += element[i]

        return result
        """
        :type strs: List[str]
        :rtype: str
        """
        
