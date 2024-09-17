class Solution(object):
    def uncommonFromSentences(self, s1, s2):

        list1 = s1.split(" ")
        list2 = s2.split(" ")
        dict1 = defaultdict(int)
        for w in list1:
            dict1[w] += 1
        for w in list2:
            dict1[w] += 1
        result = []
        for key,val in dict1.items():
            if val == 1:
                result.append(key)
        return result
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        
